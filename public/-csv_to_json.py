import csv
import json

def read_csv_and_convert_to_json(csv_filename, json_filename):
    data = {"cn": [], "en": []}

    with open(csv_filename, "r", encoding="utf-8") as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)  # Skip the header row, if present

        for row in csv_reader:
            # Check if the row has at least two elements (key and value)
            if len(row) >= 2:
                data["en"].append([row[0], row[1]])

    with open(json_filename, "w", encoding="utf-8") as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=2)

# Прочитаем данные из `p.csv` и запишем в `p.json`
read_csv_and_convert_to_json("prompts export.csv", "prompts.json")
