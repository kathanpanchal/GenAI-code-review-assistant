import os
import requests

from dotenv import load_dotenv

load_dotenv()


class GitHubClient:

    def __init__(self):
        token = os.getenv("GITHUB_TOKEN")

        self.headers = {
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github+json"
        }
    def post_issue_comment(self,repo_name,pr_number,comment_body):

        url = (
            f"https://api.github.com/repos/"
            f"{repo_name}/issues/{pr_number}/comments"
        )

        payload = {
            "body": comment_body
        }

        response = requests.post(
            url,
            headers=self.headers,
            json=payload
        )

        response.raise_for_status()

        return response.json()
    

    def get_pull_request_diff(
        self,
        repo_name: str,
        pr_number: int
    ) -> str:

        url = (
            f"https://api.github.com/repos/"
            f"{repo_name}/pulls/{pr_number}"
        )

        headers = {
            **self.headers,
            "Accept": "application/vnd.github.diff"
        }

        response = requests.get(
            url,
            headers=headers
        )

        response.raise_for_status()

        return response.text
    

    def get_issue_comments(
        self,
        repo_name,
        pr_number
    ):

        url = (
            f"https://api.github.com/repos/"
            f"{repo_name}/issues/{pr_number}/comments"
        )

        response = requests.get(
            url,
            headers=self.headers
        )

        response.raise_for_status()

        return response.json()
    
    def update_issue_comment(
        self,
        repo_name,
        comment_id,
        comment_body
    ):

        url = (
            f"https://api.github.com/repos/"
            f"{repo_name}/issues/comments/{comment_id}"
        )

        payload = {
            "body": comment_body
        }

        response = requests.patch(
            url,
            headers=self.headers,
            json=payload
        )

        response.raise_for_status()

        return response.json()