import csv

def read_csv_path(csv_path):
    """
    Reads a CSV file and returns a list of dictionaries.
    """
    try:
        with open(csv_path, encoding="utf-8") as f:
            reader = csv.DictReader(f)
            return list(reader)
    except FileNotFoundError:
        print(f"Error: The file {csv_path} was not found.")