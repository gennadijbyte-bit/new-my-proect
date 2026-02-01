import pytest

from src.masks import *


@pytest.mark.parametrize(
    "number_card, mask_number_card",
    [
        ("7000792289606361", "7000 79** **** 6361"),
        ("1111111111111111", "1111 11** **** 1111"),
        ("7700792289606377", "7700 79** **** 6377"),
    ],
)
def test_get_mask_card_number(number_card: str, mask_number_card: str) -> None:
    assert get_mask_card_number(number_card) == mask_number_card


@pytest.mark.parametrize(
    "number_bank_account, mask_number_bank_account",
    [
        ("73654108430135874305", "**4305"),
        ("11111111111111111111", "**1111"),
        ("77007922896063776677", "**6677"),
    ],
)
def test_get_mask_account(number_bank_account: str, mask_number_bank_account: str) -> None:
    assert get_mask_account(number_bank_account) == mask_number_bank_account


def test_get_mask_account_invalid() -> None:
    with pytest.raises(ValueError):
        get_mask_account("poetry1234567891234567711335")


def test_get_mask_card_number_invalid() -> None:
    with pytest.raises(ValueError):
        get_mask_card_number("12345678912345677")


def test_get_mask_account_invalid_2() -> None:
    with pytest.raises(ValueError):
        get_mask_account("")


def test_get_mask_card_number_invalid_2() -> None:
    with pytest.raises(ValueError):
        get_mask_card_number("")
