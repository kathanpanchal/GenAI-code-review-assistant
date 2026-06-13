def format_review(review_data):

    lines = []
    lines.append("<!-- GENAI_REVIEW -->")
    lines.append("## 🤖 GenAI Code Review")
    lines.append("")

    for issue in review_data["issues"]:

        lines.append(
            f"### {issue['severity'].upper()} | "
            f"{issue['category'].upper()}"
        )

        lines.append(
            f"File: {issue['file']}"
        )

        lines.append(
            issue["comment"]
        )

        lines.append("")

    return "\n".join(lines)