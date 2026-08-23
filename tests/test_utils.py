from unittest.mock import patch

from src.utils import amount_transactions, transactions


def test_transactions():
    assert transactions("tests/test.json") == [{"id": 441945886}]
    assert transactions("") == []
    assert transactions("tests/empty.json") == []


def test_amount_transactions():
    transaction1 = {"operationAmount": {"amount": "31957.58", "currency": {"code": "RUB"}}}
    assert amount_transactions(transaction1) == 31957.58
    transaction2 = {"operationAmount": {"amount": "1", "currency": {"code": "USD"}}}
    with patch("src.utils.exchange") as mock:
        mock.return_value = 100.0
        assert amount_transactions(transaction2) == 100.0


# def exchange(currency: str, amount: Union[float, int]) -> float:
