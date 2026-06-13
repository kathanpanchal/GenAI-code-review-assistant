from app.github.github_client import GitHubClient
from app.utils.review_formatter import format_review

client = GitHubClient()

repo = "kathanpanchal/genai-code-review-test"

pr_number = 1

review = {
    "issues": [
        {
            "severity": "high",
            "category": "bug",
            "file": "test.py",
            "comment": "Potential division by zero."
        }
    ]
}

comment = format_review(
    review
)

client.post_issue_comment(
    repo,
    pr_number,
    comment
)

print("Comment posted.")