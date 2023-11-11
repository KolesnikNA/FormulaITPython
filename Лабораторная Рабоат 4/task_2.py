# TODO импортировать необходимые молули
import csv
import json


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    # Считываем содержимое csv файла
    with open(INPUT_FILENAME, 'r') as csv_file:
        # Используем DictReader для чтения значений из CSV
        csv_reader = csv.DictReader(csv_file)

        # Создаем список словарей, каждый словарь представляет одну строку из CSV файла
        data_list = [row for row in csv_reader]

    # Сериализовываем в файл JSON с отступами равными 4
    with open(OUTPUT_FILENAME, 'w', encoding='utf-8') as json_file:
        json.dump(data_list, json_file, indent=4)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
