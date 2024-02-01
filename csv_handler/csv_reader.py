import csv
class CSVReader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.headers = []
        self.data = []

    def read_csv(self):
        with open(self.file_path, 'r', newline='') as csv_file:
            csv_reader = csv.reader(csv_file)

            # Read headers
            self.headers = next(csv_reader, None)

            # Read data rows
            self.data = [row for row in csv_reader]

    def get_headers(self):
        return self.headers

    def get_data(self):
        return self.data