import pytest

from src.processing import *


def test_filter_by_state(valid_information: list[Dict], valid_information_result: list[Dict] ) -> None:
    assert filter_by_state(valid_information) == valid_information_result


def test_sort_by_date(valid_information: list[Dict], valid_information_result_sort: list[Dict]) -> None:
    assert sort_by_date(valid_information) == valid_information_result_sort
