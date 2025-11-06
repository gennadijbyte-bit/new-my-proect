import masks


def mask_account_card(number_str: str) -> str:
    """Функция, которая обрабатывать информацию о картах,и о счетах."""

    name_number = number_str.split()
    str_1 = number_str[:-16]
    long_str = len(name_number[-1])
    if long_str < 20:
        number_card = str_1 + masks.get_mask_card_number(number_str[-16:])
    else:
        number_card = str_1 + masks.get_mask_account(number_str[-20:])
    return number_card


print(mask_account_card("Visa Platinum 7000792289606361"))
print(mask_account_card("Счет 73654108430135874305"))


def get_date(date_str: str) -> str:
    """функция, которая возвращает строку с датой в формате "ДД.ММ.ГГГГ"."""

    date_one = date_str[:10].split("-")
    time_id = date_one[2]
    date_one[2] = date_one[0]
    date_one[0] = time_id
    date_two = ".".join(date_one)
    return date_two



print(get_date("2024-03-11T02:26:18.671407"))
