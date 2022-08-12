import csv


def csv_reader(path):
    if not path.endswith(".csv"):
        raise FileNotFoundError(f"Extensão inválida: '{path}'")
    try:
        with open(path, 'r', encoding='utf-8') as file:
            csv_reader = csv.reader(file, delimiter=',', quotechar='"')

            data = [*csv_reader]

            return data
    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo inexistente: '{path}'")

def analyze_log(path_to_file):
    raise NotImplementedError
