from typing import List, Dict


def filter_by_state(transactions: List[Dict], state: str = "EXECUTED") -> List[Dict]:
    """Функция возвращающая новый список словарей"""

    filtered_transactions = []
    for is_first_operation in transactions:
        if is_first_operation["state"] == state:
            filtered_transactions.append((is_first_operation))
    return filtered_transactions


transactions = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]
print(filter_by_state(transactions, "EXECUTED"))


from datetime import datetime


def sort_by_date(transactions: List[Dict], descending=True) -> List[Dict]:
    """ "Функция возвращающая новый список, отсортированный по дате"""

    sorted_transactions = sorted(
        transactions, key=lambda x: datetime.strptime(x["date"], "%Y-%m-%dT%H:%M:%S.%f"), reverse=descending
    )
    return sorted_transactions


print(
    sort_by_date(
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ]
    )
)
