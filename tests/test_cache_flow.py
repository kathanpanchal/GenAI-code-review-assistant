from app.services.review_service import ReviewService

sample_diff = """
+def divide(a, b):
+    return a / b
"""

service = ReviewService()

review = service.review_diff(
    sample_diff
)

print(review)