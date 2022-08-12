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


def data_creator(path):
    data_array = csv_reader(path)
    data_dict = dict()
    foods = set()
    days = set()

    for element in data_array:
        if element[0] not in data_dict:
            data_dict[element[0]] = {
                'foods': {element[1]: 1},
                'days': {element[2]: True}
            }
        else:
            if element[1] not in data_dict[element[0]]['foods']:
                data_dict[element[0]]['foods'][element[1]] = 1
            else:
                data_dict[element[0]]['foods'][element[1]] += 1
                foods.add(element[1])
                days.add(element[2])

            if element[2] not in data_dict[element[0]]['days']:
                data_dict[element[0]]['days'][element[2]] = True

    return [data_dict, sorted(foods), sorted(days)]


def file_writer(data):
    with open('data/mkt_campaign.txt', 'a') as file:
        file.write(f'{data}\n')


def get_maria_data(data):
    most_consumed_food = ['', 0]
    for key, value in data.items():
        if key == 'maria':
            for k, v in value['foods'].items():
                if v > most_consumed_food[1]:
                    most_consumed_food[0] = k
                    most_consumed_food[1] = v
    return most_consumed_food[0]


def get_arnaldo_data(data):
    for key, value in data.items():
        if key == 'arnaldo':
            return value['foods']['hamburguer']


def get_joao_data(data):
    ans = list()
    for key, value in data[0].items():
        if key == 'joao':
            for k, v in value['foods'].items():
                data[1].remove(k)
                ans.append(set(data[1]))

            for k, v in value['days'].items():
                data[2].remove(k)
                ans.append(set(data[2]))
    return ans


def analyze_log(path_to_file):
    ans = [None for _ in range(4)]
    data_dict = data_creator(path_to_file)

    maria = get_maria_data(data_dict[0])
    ans[0] = maria
    arnaldo = get_arnaldo_data(data_dict[0])
    ans[1] = arnaldo
    joao = get_joao_data(data_dict)
    ans[2] = joao[0]
    ans[3] = joao[1]

    for answer in ans:
        file_writer(answer)
