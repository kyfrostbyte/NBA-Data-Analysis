import csv

class CSVReader:
    def __init__(self):
        self.data = {}

    def read_csv(self, file_path):
        with open(file_path, 'r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            data = list(reader)
            self.data[file_path] = data
            return data

    def write_csv(self, file_path, data):
        with open(file_path, 'w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)
            self.data[file_path] = data

