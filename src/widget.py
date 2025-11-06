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
