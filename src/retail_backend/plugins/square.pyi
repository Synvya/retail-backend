# pylint: disable=missing-docstring,unused-argument
"""Type stubs for Square plugin."""  # noqa: D100

from typing import Any, Generator

from fastapi import APIRouter
from sqlalchemy.orm import Session
from square.client import Client
from synvya_sdk import Profile

from retail_backend.core.auth import TokenData
from retail_backend.core.models import OAuthToken
from retail_backend.core.settings import SquareSettings

router: APIRouter

def get_db() -> Generator[Session, None, None]: ...
def get_square_credentials(
    current_merchant: TokenData,
    db: Session,
) -> OAuthToken: ...
def create_square_router(
    client: Client,
    settings: SquareSettings,
    square_base_url: str,
) -> APIRouter: ...
def get_merchant_info(client: Client) -> dict[str, Any]: ...
def populate_synvya_profile(merchant_data: dict[str, Any], private_key: str) -> Profile: ...
