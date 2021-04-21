# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import requests

from async_db.config import url
from db_operation import insert_data, insert_data_rfkm_no
from generate_dict import compute_all, compute_score, compute_all_fs, compute_all_rkfm_no
# from get_data import get_data_from_api


def load_json(path):
    with open(path,'r') as file:
        data = json.load(file)
    return data

def get_request(url,date):
    data = requests.get(url)
    return data.content
# TODO:// переписать с учетом принятя массивов
"""первая исправленная методичка"""
def start_script_method_1():
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
            print(e)
            res_not_insert.append(data[d]['id'])
    print('start insert data')
    print(res_not_insert)
    insert_data(res_new)
    return res_insert, res_not_insert

"""вторая методичка"""
def start_script_method_no():
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
            result = compute_all_fs(data[d])
            res_new.append((result,))
        except Exception as e:
            print(e, data[d]['id'])
            res_not_insert.append(data[d]['id'])
    print('start insert data')
    print(res_new)
    # insert_data(res_new)
    return res_insert, res_not_insert

""""""


def start_script_method_rfkm_no(lst=[], org=''):
    print('start_script')
    path = r'data.json'
    # data = get_data_from_api(lst=lst, org=org)
    # requests_data = get_request(url, '')
    data = load_json(path)
    # data = json.loads(requests_data)
    res_insert = []
    res_not_insert = []
    res_new = []
    for ind, d in enumerate(data):
        print(d)
        try:
            print(ind, d)
            result = compute_all_rkfm_no(data[d], id_=d)
            # result_score = compute_score_rkfm_no(result)
            res_new.append((result, None))
        except Exception as e:
            print(e, data[d]['id'])
            res_not_insert.append(data[d]['id'])
    print('start insert data')
    print(res_new)
    insert_data_rfkm_no(res_new)
    return res_insert, res_not_insert



# Press the green button in the gutter to run the script.
import json
# 'pfu_3', 'pfu_4', 'pfu_5'
if __name__ == '__main__':
    # pass
    start_script_method_rfkm_no(lst=['pfu_1', 'pfu_2'], org='001X3239|001X8880')
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
