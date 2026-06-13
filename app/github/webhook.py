import os

from fastapi import APIRouter
from fastapi import Request
from fastapi import HTTPException

from app.services.review_service import ReviewService
from app.utils.signature_verifier import (
    verify_signature
)

router = APIRouter()

review_service = ReviewService()


@router.post("/webhook")
async def github_webhook(request: Request):

    body = await request.body()

    signature = request.headers.get(
        "X-Hub-Signature-256"
    )

    secret = os.getenv(
        "GITHUB_WEBHOOK_SECRET"
    )

    if not verify_signature(
        body,
        signature,
        secret
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid signature"
        )

    payload = await request.json()

    action = payload.get("action")

    if action not in [
        "opened",
        "edited",
        "synchronize"
    ]:
        return {"status": "ignored"}

    repo = payload["repository"]

    pr = payload["pull_request"]

    repo_name = repo["full_name"]

    pr_number = pr["number"]

    review_service.review_pull_request(
        repo_name,
        pr_number
    )

    return {"status": "received"}