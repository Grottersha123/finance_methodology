# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import json
import requests

from config import url
from db_operation import insert_data
from generate_dict import compute_all, compute_score
import time

def load_json(path):
    with open(path,'r') as file:
        data = json.load(file)
    return data

def get_request(url,date):
    data = requests.get(url)
    return data.content
# TODO:// переписать с учетом принятя массивов

def start_script():
    print('start_script')
    path = r'example.json'
    # requests_data = get_request(url, '')
    data = load_json(path)
    # data = json.loads(requests_data)
    res_insert = []
    res_not_insert = []
    res_new = []
    for ind, d in enumerate(data):
        try:
            print(ind, data[d]['id'])
            result = compute_all(data[d])
            result_score = compute_score(result)
            res_new.append((result, result_score))
        except Exception as e:
            print(e)
            res_not_insert.append(data[d]['id'])
    print('start insert data')
    print(res_not_insert)
    insert_data(res_new)
    return res_insert, res_not_insert

def start_script_1():
    print('start_script')
    path = r'example.json'
    requests_data = get_request(url, '')
    # data = load_json(path)
    data = json.loads(requests_data)
    res_insert = []
    res_not_insert = []
    res_new = []
    for ind, d in enumerate(data):
        try:
            print(ind, data[d]['id'])
            result = compute_all(data[d])
            result_score = compute_score(result)
            res_new.append((result, result_score))
        except Exception as e:
            print(e, data[d]['id'])
            res_not_insert.append(data[d]['id'])
    print('start insert data')
    print(res_new)
    insert_data(res_new)
    return res_insert, res_not_insert




# Press the green button in the gutter to run the script.
import json
if __name__ == '__main__':
    pass
    # path = r'example.json'
    #
    # requests_data = get_request(url, '')
    # # data = load_json(path)
    # data = json.loads(requests_data)
    # for ind, d in enumerate(data):
    #     print(ind, data[d]['id'])
    #     result = compute_all(data[d])
    #     result_score = compute_score(result)
    #     insert_data(result, result_score)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
