import json
import csv
import os

def convert_json_to_csv(json_file, csv_file):
    # Удаляем файл csv, если он уже существует
    if os.path.exists(csv_file):
        os.remove(csv_file)

    # Читаем данные из json файла
    with open(json_file, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Записываем данные в csv файл
    with open(csv_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for item in data['en']:
            writer.writerow(item)

    print(f'Файл {csv_file} успешно создан и заполнен данными.')

# Пример использования функции
json_file = 'prompts.json'
csv_file = 'prompts export.csv'
convert_json_to_csv(json_file, csv_file)
