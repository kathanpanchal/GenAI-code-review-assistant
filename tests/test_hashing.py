from app.cache.cache_manager import CacheManager

code = """
def add(a, b):
    return a + b
"""
hash_value = CacheManager.generate_hash(code)

print(f"Hash of the code: {hash_value}")
