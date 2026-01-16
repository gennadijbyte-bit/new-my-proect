from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(number_str: str) -> str:
    """Функция, которая обрабатывать информацию о картах,и о счетах."""

    ind = 0
    number_card = ""
    for i in range(len(number_str) - 1, 1, -1):
        if number_str[i] == " ":
            ind = i
            break
    long_str = number_str[ind + 1 :]
    if (len(long_str) < 16 or len(long_str) > 16) and number_str[:ind] != "Счет":
        number_card = get_mask_card_number(number_str[ind + 1 :])
    if (len(long_str) < 20 or len(long_str) > 20) and number_str[:ind] == "Счет":
        number_card = get_mask_account(number_str[ind + 1 :])
    if len(long_str) == 16:
        number_card = number_str[:ind] + " " + get_mask_card_number(number_str[ind + 1 :])
    if len(long_str) == 20:
        number_card = number_str[:ind] + " " + get_mask_account(number_str[ind + 1 :])
    if len(long_str) == 20 and number_str[:ind] != "Счет":
        number_card = "Введите правильно слово <Счет>"
    return number_card


mask_account_card("Visa Platinum 7000792289606368")
mask_account_card("Счет 73654108430135874305")


def get_date(date_str: str) -> str:
    """функция, которая возвращает строку с датой в формате "ДД.ММ.ГГГГ"."""

    date_one = date_str[:10].split("-")
    time_id = date_one[2]
    date_one[2] = date_one[0]
    date_one[0] = time_id
    date_two = ".".join(date_one)
    return date_two


print(get_date("2024-03-11T02:26:18.671407"))
