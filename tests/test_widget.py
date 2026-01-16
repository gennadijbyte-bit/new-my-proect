import pytest

from src.widget import *


@pytest.mark.parametrize(
    "name_number_card, mask_name_number_card",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Visa Platinum-2025 7000792289606361", "Visa Platinum-2025 7000 79** **** 6361"),
        ("Счет 73654108430135874305", "Счет **4305"),
    ],
)
def test_mask_account_card(name_number_card: str, mask_name_number_card: str) -> None:
    assert mask_account_card(name_number_card) == mask_name_number_card


@pytest.mark.parametrize(
    "long_date, short_date",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
    ],
)
def test_get_date(long_date: str, short_date:str) -> None:
    assert get_date(long_date) == short_date
