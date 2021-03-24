# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import json
import requests

from config import url
from db_operation import insert_data
from generate_dict import compute_all, compute_score


def load_json(path):
    with open(path,'r') as file:
        data = json.load(file)
    return data

def get_request(url,date):
    data = requests.get(url)
    return data.content
# TODO:// переписать с учетом принятя массивов


# Press the green button in the gutter to run the script.
import json
if __name__ == '__main__':
    path = r'example.json'

    requests_data = get_request(url, '')
    # data = load_json(path)
    data = json.loads(requests_data)
    for ind, d in enumerate(data):
        print(ind, data[d]['id'])
        result = compute_all(data[d])
        result_score = compute_score(result)
        insert_data(result, result_score)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
