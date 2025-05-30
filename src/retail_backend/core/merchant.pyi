# pylint: disable=missing-docstring,unused-argument
"""Fetch merchant profile from Square and prepare a Synvya Profile."""

from retail_backend.core.models import MerchantProfile
from retail_backend.core.settings import Provider

async def get_nostr_profile(private_key: str) -> MerchantProfile: ...
async def set_nostr_profile(profile: MerchantProfile, private_key: str) -> None: ...
async def set_nostr_stall(provider: Provider, location: dict, private_key: str) -> bool: ...
async def set_nostr_products(
    provider: Provider,
    products: list[dict],
    categories: list[dict],
    images: list[dict],
    private_key: str,
) -> dict: ...
def _set_nostr_stall_square(location: dict, private_key: str) -> bool: ...
def _set_nostr_products_square(
    products: list[dict], categories: list[dict], images: list[dict], private_key: str
) -> dict: ...
