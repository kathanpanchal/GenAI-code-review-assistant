from app.llm.reviewer import GeminiReviewer

import os
from dotenv import load_dotenv

load_dotenv()

key = os.getenv("GEMINI_API_KEY")

print("Loaded key:", key[:10] + "...")
sample_diff = """
+def divide(a, b):
+    return a / b
"""

reviewer = GeminiReviewer()

result = reviewer.review_diff(sample_diff)

print(result)