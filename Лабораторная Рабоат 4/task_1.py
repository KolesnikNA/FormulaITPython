# TODO решите задачу
import json

def task() -> float:
    # Чтение данных из файла JSON
    with open('input.json', 'r') as file:
        data = json.load(file)

    # Вычислние произведений score * weight
    total_sum = sum(item["score"] * item["weight"] for item in data)

    # Округление суммы до 3 знаков после запятой
    rounded_sum = round(total_sum, 3)

    return rounded_sum


print(task())
