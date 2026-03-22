import base64
import os
from email.utils import parseaddr
from typing import Any

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

from email_process.gmail.models import UnprocessedEmail

SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]


def get_service() -> Any:
    creds = None
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)
        with open("token.json", "w") as f:
            f.write(creds.to_json())
    return build("gmail", "v1", credentials=creds)


def list_emails(service: Any, max_results: int = 10, query: str = "in:inbox") -> list[UnprocessedEmail]:
    """Ritorna lista di {id, snippet}"""
    result = service.users().messages().list(
        userId="me", maxResults=max_results, q=query
    ).execute()
    messages = result.get("messages", [])
    emails = []
    for msg in messages:


        detail = service.users().messages().get(
            userId="me", id=msg["id"], format="metadata",
            metadataHeaders=["From", "Subject", "Date"]
        ).execute()
        headers = {h["name"]: h["value"] for h in detail["payload"]["headers"]}
        from_email = headers.get("From", "")
        emails.append(UnprocessedEmail(
            message_id=msg["id"],
            from_=from_email,
            subject=headers.get("Subject"),
        ))
    return emails


def get_email_body(service: Any, msg_id: str) -> str:
    """Ritorna il body plain text di una email"""
    msg = service.users().messages().get(
        userId="me", id=msg_id, format="full"
    ).execute()
    payload = msg["payload"]
    return _extract_body(payload, "text/plain") or _extract_body(payload, "text/html") or msg.get("snippet", "")


def _extract_body(payload: dict, mime_type: str) -> str:
    if payload.get("mimeType") == mime_type:
        data = payload["body"].get("data", "")
        if data:
            padded = data + "=" * (-len(data) % 4)
            return base64.urlsafe_b64decode(padded).decode("utf-8", errors="replace")
    for part in payload.get("parts", []):
        result = _extract_body(part, mime_type)
        if result:
            return result
    return ""