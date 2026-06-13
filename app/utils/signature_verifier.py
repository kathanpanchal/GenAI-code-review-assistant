import hmac
import hashlib


def verify_signature(
    payload_body: bytes,
    signature_header: str,
    secret: str
) -> bool:

    expected_signature = "sha256=" + hmac.new(
        secret.encode(),
        payload_body,
        hashlib.sha256
    ).hexdigest()

    return hmac.compare_digest(
        expected_signature,
        signature_header
    )