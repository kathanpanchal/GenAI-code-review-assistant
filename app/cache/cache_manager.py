import hashlib


class CacheManager:

    @staticmethod
    def normalize_code(code_text: str ) -> str:

        lines = [
            line.strip()
            for line in code_text.splitlines()
            if line.strip()
        ]

        return "\n".join(lines)

    @classmethod
    def generate_hash(
        cls,
        code_text: str
    ) -> str:

        normalized = cls.normalize_code(
            code_text
        )

        return hashlib.sha256(
            normalized.encode()
        ).hexdigest()