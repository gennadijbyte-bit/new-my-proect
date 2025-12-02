def get_mask_card_number(number1: str) -> str:
    """Функция маскировки номера банковской карты."""

    exit_number1 = number1[:4] + " " + number1[4:6] + "**" + " " + "****" + " " + number1[-4:]
    return exit_number1


get_mask_card_number("7000792289606361")


def get_mask_account(number2: str) -> str:
    """Функцию маскировки номера банковского счета"""

    exit_number2 = "**" + " " + number2[-4:]
    return exit_number2


get_mask_account("73654108430135874305")
