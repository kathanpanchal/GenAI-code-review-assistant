const errorDetailsMap = {
  invalid_pr_url: {
    title: "Invalid Pull Request URL",
    suggestions: [
      "Check for typos in the URL path.",
      "Ensure the URL matches the format: https://github.com/owner/repository/pull/number",
      "Ensure you are referencing a public pull request, not a main repository branch or issue."
    ]
  },
  github_api_error: {
    title: "GitHub Access Failure",
    suggestions: [
      "Verify the repository is public (private repositories require a configured GITHUB_TOKEN on the backend).",
      "Check if your GITHUB_TOKEN environment variable is set and has read access to the target repository.",
      "The GitHub API rate limit may have been reached. Please wait a few minutes and try again."
    ]
  },
  gemini_api_error: {
    title: "Gemini AI Failure",
    suggestions: [
      "Ensure the GEMINI_API_KEY environment variable is correctly configured in your server's .env file.",
      "Verify that the Gemini API is active and you have not exceeded your quota limits.",
      "The code review payload may have hit size limits. Try analyzing a smaller PR diff."
    ]
  },
  internal_error: {
    title: "Internal Server Error",
    suggestions: [
      "Check if the backend FastAPI server is running.",
      "Verify that the PostgreSQL database is online and reachable by the backend.",
      "Examine the backend logs for any unhandled exceptions or connection timeouts."
    ]
  },
  invalid_request: {
    title: "Invalid Request",
    suggestions: [
      "The payload sent to the backend was malformed or validation failed.",
      "Please refresh the page and try submitting the PR URL again."
    ]
  }
}

export default function ErrorState({ error, onRetry }) {
  const message = typeof error === 'string' ? error : error?.message
  const code = typeof error === 'string' ? null : error?.code

  const details = errorDetailsMap[code] || {
    title: "Unable to analyze PR",
    suggestions: [
      "Verify the Pull Request exists and the repository is public.",
      "Check if the GitHub API rate limit has been exceeded.",
      "Ensure the Pull Request diff is not too large.",
      "Check backend server and database status."
    ]
  }

  return (
    <div className="glass rounded-xl border border-rose-500/30 bg-gradient-to-br from-rose-950/20 to-slate-950/40 p-6 shadow-xl backdrop-blur-xl">
      <div className="flex items-start gap-4">
        <div className="flex h-11 w-11 shrink-0 items-center justify-center rounded-lg bg-rose-500/10 text-rose-400">
          <IconAlert />
        </div>
        
        <div className="flex-1">
          <h3 className="text-lg font-bold text-rose-300">{details.title}</h3>
          <p className="mt-2 text-slate-300 leading-relaxed text-sm">{message}</p>
          
          <div className="mt-4">
            <h4 className="text-xs font-semibold uppercase tracking-wider text-slate-400">Recommended Steps:</h4>
            <ul className="mt-2 space-y-2">
              {details.suggestions.map((suggestion, index) => (
                <li key={index} className="flex items-start gap-2 text-sm text-slate-400">
                  <span className="mt-1.5 h-1.5 w-1.5 shrink-0 rounded-full bg-rose-400/70" />
                  <span>{suggestion}</span>
                </li>
              ))}
            </ul>
          </div>
          
          {onRetry && (
            <button
              onClick={onRetry}
              className="mt-6 rounded-lg bg-rose-500/20 border border-rose-500/40 px-5 py-2 text-sm font-semibold text-rose-200 transition hover:bg-rose-500/35 hover:text-white"
            >
              Dismiss
            </button>
          )}
        </div>
      </div>
    </div>
  )
}

function IconAlert() {
  return (
    <svg className="h-6 w-6" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" aria-hidden="true">
      <path strokeLinecap="round" strokeLinejoin="round" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z" />
    </svg>
  )
}
