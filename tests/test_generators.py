from collections.abc import Generator

import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency(transaction):
    assert len(list(filter_by_currency(transaction, "USD"))) == 3
    assert len(list(filter_by_currency(transaction, "RUB"))) == 2
    assert len(list(filter_by_currency(transaction, ""))) == 0
    assert isinstance(filter_by_currency(transaction, "USD"), Generator)


@pytest.mark.parametrize(
    "transactions,expected_descriptions",
    [
        (transac, desc)
        for transac, desc in zip(
            [
                {
                    "id": 939719570,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                    "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод организации",
                    "from": "Счет 75106830613657916952",
                    "to": "Счет 11776614605963066702",
                },
                {
                    "id": 142264268,
                    "state": "EXECUTED",
                    "date": "2019-04-04T23:20:05.206878",
                    "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод со счета на счет",
                    "from": "Счет 19708645243227258542",
                    "to": "Счет 75651667383060284188",
                },
                {
                    "id": 873106923,
                    "state": "EXECUTED",
                    "date": "2019-03-23T01:09:46.296404",
                    "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
                    "description": "Перевод со счета на счет",
                    "from": "Счет 44812258784861134719",
                    "to": "Счет 74489636417521191160",
                },
            ],
            [
                "Перевод организации",
                "Перевод со счета на счет",
                "Перевод со счета на счет",
            ],
        )
    ],
)
def test_transaction_descriptions(transactions, expected_descriptions):
    assert next(transaction_descriptions([transactions])) == expected_descriptions


@pytest.mark.parametrize("start", [-1, 10**17])
def test_card_number_generator_invalid_start(start):
    with pytest.raises(ValueError):
        next(card_number_generator(start, 9999_9999_9999_9999))


def test_card_number_generator():
    c = card_number_generator(9998, 10003)
    assert next(c) == "0000 0000 0000 9998"
    assert next(c) == "0000 0000 0000 9999"
    assert next(c) == "0000 0000 0001 0000"
    assert next(c) == "0000 0000 0001 0001"
    assert next(c) == "0000 0000 0001 0002"
    assert next(c) == "0000 0000 0001 0003"
    with pytest.raises(StopIteration):
        next(c)
    # Проверки валидации входных параметров генератора
    generator_case_1 = card_number_generator(-1, 9999)
    with pytest.raises(ValueError):
        next(generator_case_1)
    generator_case_2 = card_number_generator(9999_9999_9999_9999 + 1, 9999)
    with pytest.raises(ValueError):
        next(generator_case_2)
    generator_case_3 = card_number_generator(1, -1)
    with pytest.raises(ValueError):
        next(generator_case_3)
    generator_case_4 = card_number_generator(1, 9999_9999_9999_9999 + 1)
    with pytest.raises(ValueError):
        next(generator_case_4)
    generator_case_5 = card_number_generator(100, 99)
    with pytest.raises(ValueError):
        next(generator_case_5)
