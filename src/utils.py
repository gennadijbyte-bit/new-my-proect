import json

from src.external_api import exchange


def transactions(path: str) -> list:
    """функция принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях"""
    try:
        with open(path, "r", encoding="utf-8") as json_file:
            data = json.load(json_file)
            if len(data) == 0:
                return []
        return list(data)
    except FileNotFoundError:
        return []
    except json.decoder.JSONDecodeError:
        return []


def amount_transactions(transaction_dict: dict) -> float:
    """функция принимает на вход транзакцию и возвращает сумму транзакции (amount) в рублях, тип данных —
    float. Если транзакция была в USD или EUR, происходит обращение к внешнему API для получения текущего курса валют
    и конвертации суммы операции в рубли"""
    operation_amount = transaction_dict.get("operationAmount", {})
    amount = float(operation_amount.get("amount", ""))
    currency = operation_amount.get("currency", {})
    code = currency.get("code", "")
    if code != "RUB":
        return exchange(code, amount)
    return amount



