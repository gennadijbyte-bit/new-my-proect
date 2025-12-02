from typing import List, Dict


def filter_by_state(transactions: List[Dict], state: str = "EXECUTED") -> List[Dict]:
    """Функция возвращающая новый список словарей"""

    new_transactions = []
    for first in transactions:
        if first["state"] == state:
            new_transactions.append((first))
    return new_transactions


transactions = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]
print(filter_by_state(transactions, "EXECUTED"))
