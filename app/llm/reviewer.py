import os
import json
import time
from dotenv import load_dotenv
from google import genai
from app.llm.base_reviewer import BaseReviewer

load_dotenv()


class GeminiReviewer(BaseReviewer):

    def __init__(self):
        self.client = genai.Client(
            api_key=os.getenv("GEMINI_API_KEY")
        )

    def clean_json_response(self, text):
        text = text.replace("```json", "")
        text = text.replace("```", "")
        return text.strip()

    def review_diff(self, diff_text):

        prompt = f"""
        Review this GitHub Pull Request diff.

        Return ONLY valid JSON.

        Schema:

        {{
        "issues": [
            {{
            "severity": "low|medium|high",
            "category": "bug|security|performance|maintainability",
            "file": "filename.py",
            "comment": "review comment"
            }}
        ]
        }}

        Code Diff:

        {diff_text}
        """

        response = self.client.models.generate_content(
            model="gemini-2.5-flash-lite",
            contents=prompt
            )

        cleaned = self.clean_json_response(
            response.text
        )

        return json.loads(cleaned)