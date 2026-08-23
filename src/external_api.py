import os
from typing import Union

import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")


def exchange(currency: str, amount: Union[float, int]) -> float:
    url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}"

    payload: dict = {}
    headers = {"apikey": api_key}

    response = requests.request("GET", url, headers=headers, data=payload)

    if response.status_code != 200:
        print(f"Error: {response.status_code}, {response.text}")

    result = response.json()

    return float(result["result"])


if __name__ == "__main__":
    currency = "EUR"
    amount = 100
    result = exchange(currency, amount)
    print(f"{amount} {currency} = {result} RUB")
