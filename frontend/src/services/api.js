const API_BASE_URL = "/api";

export async function reviewPullRequest(
  prUrl,
  onProgress = () => {}
) {
  const response =
    await fetch(
      `${API_BASE_URL}/review/stream`,
      {
        method: "POST",
        headers: {
          "Content-Type":
            "application/json"
        },
        body: JSON.stringify({
          pr_url: prUrl
        })
      }
    );

  if (!response.ok) {
    const { message, code } = await getErrorMessageAndCode(response);
    const err = new Error(message);
    err.code = code;
    throw err;
  }

  if (!response.body) {
    throw new Error("Unable to read the review response.");
  }

  const reader = response.body.getReader();
  const decoder = new TextDecoder();
  let buffer = "";
  let review = null;

  while (true) {
    const { done, value } = await reader.read();
    buffer += decoder.decode(value || new Uint8Array(), { stream: !done });

    const lines = buffer.split("\n");
    buffer = done ? "" : lines.pop();

    for (const line of lines) {
      if (!line.trim()) continue;

      const event = JSON.parse(line);

      if (event.type === "progress") {
        onProgress(event.step);
      } else if (event.type === "result") {
        review = event.data;
      } else if (event.type === "error") {
        const err = new Error(event.error?.message || "Unable to analyze the PR.");
        err.code = event.error?.code || "review_error";
        throw err;
      }
    }

    if (done) break;
  }

  if (!review) {
    throw new Error("The review could not be completed.");
  }

  return review;
}

export async function getMetrics() {
  const response =
    await fetch(
      `${API_BASE_URL}/metrics`
    );

  if (!response.ok) {
    throw new Error(
      "Unable to load dashboard metrics."
    );
  }

  return response.json();
}

async function getErrorMessageAndCode(response) {
  try {
    const payload = await response.json();
    return {
      message: payload?.error?.message || payload?.detail || "Unable to analyze the PR.",
      code: payload?.error?.code || "internal_error"
    };
  } catch {
    return {
      message: "Unable to analyze the PR. Please try again.",
      code: "internal_error"
    };
  }
}
