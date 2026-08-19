from datetime import datetime
from functools import wraps
from typing import Any, Callable, Optional


def write_log(filename: str, message: str) -> None:
    """Вспомогательная функция для вывода логов в файл или консоль"""

    if filename != "":
        with open(filename, "a", encoding="utf-8") as f:
            f.write(message + "\n")
    else:
        print(message)


def log(filename: Optional[str] = None) -> Any:
    """Декоратор, который автоматически логирует начало, конец выполнения функции,
    а также ее результаты или возникшие ошибки"""

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            start = datetime.now()
            message_start = f"{func.__name__} start {start:%Y-%m-%d %H:%M:%S}\n"
            try:
                result = func(*args, **kwargs)
                message_result = f"{func.__name__} ok\n"
                end = datetime.now()
                message_end = f"{func.__name__} end {end:%Y-%m-%d %H:%M:%S}\n"
                message = f"{message_start}{message_result}{message_end}"
                write_log(filename, message)
                return result
            except Exception as e:
                end = datetime.now()
                message_result = f"{func.__name__} error: {str(e)}. Inputs: {args}, {kwargs}\n"
                message_end = f"{func.__name__} end {end:%Y-%m-%d %H:%M:%S}\n"
                message = f"{message_start}{message_result}{message_end}"
                write_log(filename, message)
                raise

        return wrapper

    return decorator
