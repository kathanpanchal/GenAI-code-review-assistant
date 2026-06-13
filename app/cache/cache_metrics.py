class CacheMetrics:

    cache_hits = 0
    cache_misses = 0

    @classmethod
    def record_hit(cls):
        cls.cache_hits += 1

    @classmethod
    def record_miss(cls):
        cls.cache_misses += 1

    @classmethod
    def get_stats(cls):

        total = (cls.cache_hits + cls.cache_misses)

        hit_rate = 0

        if total > 0:
            hit_rate = (
                cls.cache_hits
                / total
            ) * 100

        return {
            "hits": cls.cache_hits,
            "misses": cls.cache_misses,
            "hit_rate": round(hit_rate, 2)
        }