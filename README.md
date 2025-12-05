# Мой потрясающий проект
## Описание
   Проект предназначен для обработки банковских операций, фильтрации по состоянию ключа и сортировке по дате
## Установка
		1. Убедитесь, что у вас установлен Python версии 3.8 или выше.
		2. Установите необходимые зависимости с помощью команды:
                pip install -r requirements.txt
## Использование

Пример функции filter_by_state:


from src.processing import filter_by_state

operations = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 59402872, 'state': 'CANCELLED', 'date': '2018-09-17T21:27:25.241241'}
]

filtered_operations = filter_by_state(operations)
print(filtered_operations)

Пример функции sort_by_date:


from src.processing import sort_by_date

operations = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 59402872, 'state': 'CANCELLED', 'date': '2018-09-17T21:27:25.241241'}
]

sorted_operations = sort_by_date(operations)
print(sorted_operations)

## Лицензия
MIT License
## Контакты
Электронная почта сопровождающего: gennadij.byte@domain.com
