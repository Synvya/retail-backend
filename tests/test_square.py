"""
This module contains tests for the Square API integration, specifically focusing on the
functionality of fetching and preparing user profiles from the Square API.

The `test_fetch_and_prepare_profile` function tests the integration by attempting to
fetch a user profile using a predefined OAuth token. It verifies that the profile is
created successfully and prints the public and private keys. In case of an error,
it captures and prints the error message.
"""

from unittest.mock import MagicMock

import pytest
from sqlalchemy.orm import Session
from square.client import Client
from synvya_sdk import Profile

from retail_backend.core.database import SessionLocal
from retail_backend.core.dependencies import get_square_client
from retail_backend.core.models import SquareMerchantCredentials
from retail_backend.plugins.square import get_merchant_info


@pytest.fixture(scope="session", name="client")
def client_fixture() -> Client:
    """
    Fixture to get the Square client.
    """
    return get_square_client()


def retrieve_oauth_token() -> tuple[str, str]:
    """
    Retrieves the OAuth token securely from the database.
    Args:
        None
    Returns:
        tuple[str, str]: A tuple containing the access token and the environment.
    Raises:
        RuntimeError: If the OAuth token is not found in the database.
    """
    db: Session = SessionLocal()
    try:
        token_entry = db.query(SquareMerchantCredentials).filter_by(environment="sandbox").first()
        if token_entry:
            return str(token_entry.square_merchant_token), str(token_entry.environment)
        else:
            raise RuntimeError("OAuth token not found in the database.")
    finally:
        db.close()


def test_get_merchant_info(client: Client) -> None:
    """
    Test get_merchant_info.
    """
    # Mock the Square API response
    mock_merchant = {
        "id": "MLMXWMGK6R2V8",
        "business_name": "Test Business",
        "country": "US",
        "language_code": "en-US",
        "currency": "USD",
    }
    client.merchants.retrieve_merchant = MagicMock(
        return_value=MagicMock(
            is_success=MagicMock(return_value=True),
            body=MagicMock(get=MagicMock(return_value=mock_merchant)),
        )
    )

    # Call the function
    merchant_info = get_merchant_info(client)

    # Verify the result
    assert merchant_info == mock_merchant
    client.merchants.retrieve_merchant.assert_called_once_with(merchant_id="me")
