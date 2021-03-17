# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import json

from financial_methodology import average_percent, max_percent, compute_1, divided_two_minus_percent, \
    compute_average_percent, sum_6_abs_percent, divided_2_percent, sum_3_abs_percent, sum_3_percent, divided_12_percent, \
    divided_12_parametr_3_percent, divided_12_coef_parametr_3_percent, sum_2_parametr_percent


def load_json(path):
    with open(path,'r') as file:
        data = json.load(file)
    return data

def cnv(lst):
    return list(map(float, lst))

def compute_all(data):

    data_20 = data['01012020']
    data_21 = data['01012021']

    compute_dict = {
        'd_t_delta': average_percent(
            *cnv(
            [data_21['d_t'], data_20['d_t']]
            )
        ),
        'd_t_max_percent_20': max_percent(
            *cnv(
                [data_20['d_t_'], data_20['d_t_gz'], data_20['d_t_ic'], data_20['d_t_oms'], data_20['d_t_pdd']]
            )
        ),
        'd_t_max_percent_21': max_percent(
            *cnv(
                [data_21['d_t_'], data_21['d_t_gz'], data_21['d_t_ic'], data_21['d_t_oms'], data_21['d_t_pdd']]
            )
        ),
        'p_t_delta': average_percent(
            *cnv(
                [data_21['p_t'], data_20['p_t']]
            )
        ),

        'fot_t_delta': average_percent(
            *cnv(
                [data_21['fot_t'], data_20['fot_t']]
            )
        ),
        'op_6': compute_1(
            *cnv(
                [data_21['os_t_ng'],data_21['d_t'], data_20['p_t']]
            )
        ),
        'op_7': divided_two_minus_percent(
            *cnv(
                [data_21['d_t'], data_21['p_t']]
            )
        ),
        'op_9': sum_6_abs_percent(
            *cnv(
                [data_21['os_t_pdd'], data_21['d_t_pdd'], data_21['p_t_pdd'], data_21['z_t_uv'], data_21['z_t_um']]
            )
        ),
        'pfu_3': divided_2_percent(
            *cnv(
                [data_21['d_t_o'], data_21['d_t_pdd']]
            )
        ),
        'pfu_3a': sum_3_abs_percent(
            *cnv(
                [data_21['d_t_o'], data_21['z_t_p_1_uv'], data_21['z_t_p_1_um'], data_21['d_t_p_1_pdd']]
            )
        ),
        'pfu_6': sum_3_percent(
            *cnv(
                [data_21['vla_t'], data_21['dz_t'], data_21['kz_t'], data_21['d_t_pdd']]
            )
        ),
        'pfu_4': divided_2_percent(
            *cnv(
                [data_21['kz_pr'], data_21['kz_t']]
            )
        ),
        'pfu_5': divided_2_percent(
            *cnv(
                [data_21['dz_pr'], data_21['dz_t']]
            )
        ),
        'pfu_7': divided_2_percent(
            *cnv(
                [data_21['kz_t'], data_21['d_t']]
            )
        ),
        'pfu_8': divided_2_percent(
            *cnv(
                [data_21['dz_t'], data_21['vb_t']]
            )
        ),
        'pfu_9': divided_2_percent(
            *cnv(
                [data_21['dz_t'], data_21['d_t']]
            )
        ),
        'pfu_9': divided_2_percent(
            *cnv(
                [data_21['dz_t'], data_21['d_t']]
            )
        ),
        'pfu_10_oc_1': compute_average_percent(
            *cnv(
                [data_21['os'], data_21['kz_zpvf']]
            )
        ),
        'pfu_14': divided_12_parametr_3_percent(
            *cnv(
                [data_21['kz_zp'], data_21['fot_p'], data_21['k_zp']]
            )
        ),
        'pfu_15': divided_12_coef_parametr_3_percent(
            *cnv(
                [data_21['kz_vf'], data_21['fot_p'], data_21['k_fp']]
            )
        ),
        'lp_1': divided_2_percent(
            *cnv(
                [data_21['p_f'], data_21['p_p']]
            )
        ),
        'lp_2': sum_2_parametr_percent(
            *cnv(
                [data_21['kz_zp'], data_21['fot_f'],data_21['fot_p']]
            )
        ),

    }
    # 88 стр
    calculated_dict = {
        'd_t_max_delta_max_percent': average_percent(
            *cnv(
                [compute_dict['d_t_max_percent_21'], compute_dict['d_t_max_percent_20']]
            )
        ),
        'op_7': compute_average_percent(
            *cnv(
                [compute_dict['p_t_delta'], compute_dict['d_t_delta']]
            )
        ),
        'pfu_11': divided_12_percent(
            *cnv(
                [compute_dict['pfu_10_oc_1'], data_21['p_p']]
            )
        ),
        'pfu_12_oc_2': compute_average_percent(
            *cnv(
                [compute_dict['pfu_10_oc_1'], data_21['kz_pr']]
            )
        ),
    }
    calculate_dict_1 = {
        'pfu_13': divided_12_percent(
            *cnv(
                [calculated_dict['pfu_12_oc_2'], data_21['p_p']]
            )
        ),

    }


    return calculated_dict, calculate_dict_1, compute_dict

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    path = r'example.json'
    data = load_json(path)
    result = compute_all(data['data'])
    print(result)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
