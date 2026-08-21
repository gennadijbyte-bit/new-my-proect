from typing import Any, Generator, Iterator


def filter_by_currency(
    transactions: list[dict[str, Any]], currency_code: str
) -> Generator[dict[str, Any], None, None]:
    """Фильтрация транзакций по валюте."""

    for transaction in transactions:
        transaction_currency_code = transaction["operationAmount"]["currency"]["code"]
        if transaction_currency_code == currency_code:
            yield transaction


def transaction_descriptions(transactions: list[dict[str, Any]]) -> Iterator[str]:
    """Фильтрация по описанию транзакции."""

    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(start: int, stop: int) -> Generator[str, None, None]:
    """Генерирует номера банковских карт в формате XXXX XXXX XXXX XXXX, где X — цифра номера карты."""

    if start < 0 or start > 9999_9999_9999_9999:
        raise ValueError("Старт должен быть в диапазоне от 0 до 9999_9999_9999_9999")
    if stop < 0 or stop > 9999_9999_9999_9999:
        raise ValueError("Стоп должен быть в диапазоне от 0 до 9999_9999_9999_9999")
    if start > stop:
        raise ValueError("Старт не может быть больше стопа")
    for i in range(start, stop + 1):
        s = str(i).zfill(16)
        list_s = [s[0:4], s[4:8], s[8:12], s[12:16]]
        yield " ".join(list_s)
