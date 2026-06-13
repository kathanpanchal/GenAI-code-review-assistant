from app.cache.cache_repository import CacheRepository

repo = CacheRepository()

repo.save_review(
    "abc123",
    {
        "issues": [
            {
                "severity": "high",
                "category": "bug",
                "comment": "Division by zero"
            }
        ]
    }
)

review = repo.get_review_by_hash(
    "abc123"
)

print(review)