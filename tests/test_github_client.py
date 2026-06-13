import sys
from pathlib import Path

# Add the root directory to the path so we can import app module
sys.path.insert(0, str(Path(__file__).parent.parent))

from app.github.github_client import GitHubClient

client = GitHubClient()

repo = "kathanpanchal/genai-code-review-test"

pr_number = 1

diff = client.get_pull_request_diff(
    repo,
    pr_number
)

print(diff)