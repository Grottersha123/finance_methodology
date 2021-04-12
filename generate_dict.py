from financial_methodology import average_percent, max_value, diffence, max_percent, compute_1, divided_two_minus_percent, sum_6_abs_percent, \
    divided_2_percent, sum_3_abs_percent, sum_3_percent, compute_average_percent, divided_12_parametr_3_percent, \
    divided_12_coef_parametr_3_percent, sum_2_parametr_percent, difference_abs, divided_12_percent
from score_op import score_op_1, score_op_2_3, score_op_5, score_op_7, score_op_8, score_pfu_3, score_pfu_6, \
    score_pfu_10, score_pfu_12, score_pfu_14_15, score_lp_3, score_lp_5


def cnv(lst):
    try:
        return list(map(float, lst))
    except Exception as e:
        print(e)
        return [0]


def compute_all(data):
    data_20 = data['01012020']
    data_21 = data['01012021']
    # data_year = data['year']

    compute_dict = {
        "id": data["id"],

        'op_1_d_t_delta': average_percent(
            *cnv(
            [data_21['d_t'], data_20['d_t']]
            ), a='op_1_d_t_delta',

        ),
        'op_1a': average_percent(
            *cnv(
                [data_21['d_t_1'], data_20['d_t']]
            ), a='op_1_d_t_delta',

        ),
        # Start Oleg's code
        'op_2_d_t_max_value_20': max_value(
            *cnv(
                [data_20['d_t_gz'], data_20['d_t_ic'], data_20['d_t_oms'], data_20['d_t_pdd']]
            )
        ),
        'op_2_d_t_max_value_21': max_value(
            *cnv(
                [data_21['d_t_gz'], data_21['d_t_ic'], data_21['d_t_oms'], data_21['d_t_pdd']]
            )
        ),
        'kz_pr': diffence(
            *cnv(
                [data_21['kz_pr_plus'], data_21['kz_pr_minus']]
            )
        ),
        # end Oleg's code
        'op_10_d_t_max_percent_20': max_percent(
            *cnv(
                [data_20['d_t_'], data_20['d_t_gz'], data_20['d_t_ic'], data_20['d_t_oms'], data_20['d_t_pdd']]
            )
        ),
        'op_10_d_t_max_percent_21': max_percent(
            *cnv(
                [data_21['d_t_'], data_21['d_t_gz'], data_21['d_t_ic'], data_21['d_t_oms'], data_21['d_t_pdd']]
            )
        ),
        'op_10a': max_percent(
            *cnv(
                [data_21['d_t_1'], data_21['d_t_gz_1'], data_21['d_t_ic_1'], data_21['d_t_oms_1'], data_21['d_t_pdd_1']]
            )
        ),

        'op_4_p_t_delta': average_percent(
            *cnv(
                [data_21['p_t'], data_20['p_t']]
            ),
            a='op_4_p_t_delta'
        ),
        'op_4a': average_percent(
            *cnv(
                [data_21['p_t_1'], data_20['p_t']]
            ),
            a='op_4_p_t_delta'
        ),
        'op_5': average_percent(
            *cnv(
                [data_21['fot_t'], data_20['fot_t']]
            ),
            a='op_5'
        ),
        'op_5a': average_percent(
            *cnv(
                [data_21['fot_t_1'], data_20['fot_t']]
            ),
            a='op_5'
        ),

        'fot_t_delta': average_percent(
            *cnv(
                [data_21['fot_t'], data_20['fot_t']]
            ),
            a = 'fot_t_delta'
        ),
        'op_6': compute_1(
            *cnv(
                [data_21['os_t_ng'], data_21['d_t'], data_21['p_t']]  # Oleg - change:  data_20['p_t']] →  data_21['p_t']]
            )
        ),

        'op_6a': compute_1(
            *cnv(
                [data_21['os_t_ng_1'], data_21['d_t_1'], data_21['p_t_1']]
                # Oleg - change:  data_20['p_t']] →  data_21['p_t']]
            )
        ),
        'op_7': divided_two_minus_percent(
            *cnv(
                [data_21['d_t'], data_21['p_t']]
            )
        ),
        'op_7a': divided_two_minus_percent(
            *cnv(
                [data_21['d_t_1'], data_21['p_t_1']]
            )
        ),

        'op_9': sum_6_abs_percent(
            *cnv(
                [data_21['os_t_pdd'], data_21['d_t_pdd'], data_21['p_t_pdd'], data_21['z_t_uv'], data_21['z_t_um']]
            )
        ),
        'op_9a': sum_6_abs_percent(
            *cnv(
                [data_21['os_t_pdd_1'], data_21['d_t_pdd_1'], data_21['p_t_pdd_1'], data_21['z_t_uv_1'], data_21['z_t_um_1']]
            )
        ),

        'pfu_3': divided_2_percent(
            *cnv(
                [data_21['d_t_o'], data_21.get('d_t_pdd')]
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
                [data_21['kz_pros'], data_21['kz']] # Oleg - change:  data_21['kz_pr'] → data_21['kz_pros'],
                # data_21['kz_t']] → data_21['kz']]
            )
        ),
        'pfu_5': divided_2_percent(
            *cnv(
                [data_21['dz_pros'], data_21['dz']]# Oleg - change:  data_21['dz_t'] → data_21['dz'],
            )
        ),
        'pfu_7': sum_2_parametr_percent(
            *cnv(
                [data_21['d_t_o'], data_21['kz'], data_21['d_t_']]# Oleg - change:  data_21['d_t'] → data_21['d_t_'],
                # data_21['kz_t']] → data_21['kz']]
            )
        ),
        'pfu_8': sum_2_parametr_percent(
            *cnv(
                [data_21['dz_z'], data_21['dz'], data_21['vb_t']]
                # data_21['dz_t']] → data_21['dz']]
            )
        ),
        'pfu_9': sum_2_parametr_percent(
            *cnv(
                [data_21['dz_z'], data_21['dz'], data_21['d_t_']]# Oleg - change:  data_21['d_t'] → data_21['d_t_'],
                # data_21['dz_t']] → data_21['dz']]
            )
        ),
        #
        # 'pfu_11': divided_12_percent(
        #     *cnv(
        #         [data_21['os_1'], data_21['rp']]  # Oleg - change:  data_21['d_t'] → data_21['d_t_'],
        #         # data_21['dz_t']] → data_21['dz']]
        #     )
        # ),
        # 'pfu_12': diffence(
        #     *cnv(
        #         [data_21['os_2'], data_21['rp']]  # Oleg - change:  data_21['d_t'] → data_21['d_t_'],
        #         # data_21['dz_t']] → data_21['dz']]
        #     )
        # ),
        # 'pfu_13': divided_12_percent(
        #     *cnv(
        #         [data_21['os_1'], data_21['kz_pr']]  # Oleg - change:  data_21['d_t'] → data_21['d_t_'],
        #         # data_21['dz_t']] → data_21['dz']]
        #     )
        # ),
        'pfu_10_oc_1': compute_average_percent(
            *cnv(
                [data_21['os'], data_21['kz_zpvf']]
            )
        ),
        'pfu_14': divided_12_parametr_3_percent(
            *cnv(
                [data_21['kz_zpvf'], data_21['fot_p'], data_21['k_zp']]# Oleg - change:  data_21['kz_zp'] → data_21['kz_zpvf'],
            )
        ),
        'pfu_15': divided_12_coef_parametr_3_percent(
            *cnv(
                [data_21['kz_vf'], data_21['fot_p'], data_21['k_vf']]
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
        'lp_3_ko_delta': difference_abs(
            *cnv(
                [data_21['z_1_pdd'], data_21['z_2_pdd']]
            )
        ),
        # 'pd_1_1_d1': difference_abs(
        #     *cnv(
        #         [data_21['d_tf_pdd'], data_year['pd_1_d_t_pdd'],data_21['d_tp_pdd']]
        #     )
        # ),
        # 'pd_1_2_d1': difference_abs(
        #     *cnv(
        #         [data_21['d_tf_oms'], data_year['pd_1_2_d_t_oms'], data_21['d_tp_oms']]
        #     )
        # ),
        # # TODO:// что с регистром диктов
        # 'pd_3_p1_fot_0_p_1': divided_difference_parametr_4(
        #     *cnv(
        #         [data_21['fot_tf'], data_20['fot_tf'], data_year['fot_tp'], data_year['fot_tf']]
        #     )
        # ),
        # # TODO:// что с регистром диктов
        # 'pd_4_p1_vf_0_p_2': divided_difference_parametr_4(
        #     *cnv(
        #         [data_21['vf_tf'], data_20['vf_tf'], data_year['vf_tp'], data_year['vf_tf']]
        #     )
        # ),
        # 'pd_5_p1_p_pr_0_p_2': divided_difference_parametr_4(
        #     *cnv(
        #         [data_21['p_tf'], data_20['vp_tf'], data_year['p_tp'], data_year['p_tf']]
        #     )
        # ),

    }
    # 88 стр
    calculated_dict = {
        'op_3_d_t_max_delta_max_percent': average_percent(
            *cnv(
                [compute_dict['op_2_d_t_max_value_21'], compute_dict['op_2_d_t_max_value_20']]
                # Oleg's change: [compute_dict['op_2_d_t_max_percent_21'], compute_dict['op_2_d_t_max_percent_20']] →
                # → [compute_dict['op_2_d_t_max_value_21'], compute_dict['op_2_d_t_max_value_20']]
            ),
           a='op_3_d_t_max_delta_max_percent'
        ),
        'op_8': compute_average_percent(
            *cnv(
                [compute_dict['op_4_p_t_delta'], compute_dict['op_1_d_t_delta']]
            )
        ),
        'op_8a': compute_average_percent(
            *cnv(
                [compute_dict['op_4a'], compute_dict['op_1a']]
            )
        ),
         'op_11': average_percent(
            *cnv(
                [compute_dict['op_10_d_t_max_percent_20'], compute_dict['op_10_d_t_max_percent_21']]
                # Oleg's change: [compute_dict['op_2_d_t_max_percent_21'], compute_dict['op_2_d_t_max_percent_20']] →
                # → [compute_dict['op_2_d_t_max_value_21'], compute_dict['op_2_d_t_max_value_20']]
            ),
           a='op_11'
        ),
    'op_11a': average_percent(
            *cnv(
                [compute_dict['op_10_d_t_max_percent_20'], compute_dict['op_10_d_t_max_percent_21']]
                # Oleg's change: [compute_dict['op_2_d_t_max_percent_21'], compute_dict['op_2_d_t_max_percent_20']] →
                # → [compute_dict['op_2_d_t_max_value_21'], compute_dict['op_2_d_t_max_value_20']]
            ),
           a='op_11'
        ),
        'pfu_11': divided_12_percent(
            *cnv(
                [compute_dict['pfu_10_oc_1'], data_21['p_p']]
            )
        ),
        'pfu_11a': divided_12_percent(
            *cnv(
                [compute_dict['pfu_10_oc_1'], data_21['p_p']]
            )
        ),
        'pfu_12_oc_2': compute_average_percent(
            *cnv(
                [compute_dict['pfu_10_oc_1'], compute_dict['kz_pr']]
            )
        ),
        'lp_4': divided_2_percent(
            *cnv(
                [compute_dict['lp_3_ko_delta'], data_21['d_pt_pdd']]
            )
        ),
        'lp_5': sum_2_parametr_percent(
            *cnv(
                [data_21.get('d_t_o',0), compute_dict['lp_3_ko_delta'], data_21['d_pt_pdd']]
            )
        ),
        # 'pd_2_d1': compute_divided_parametr_3(
        #     *cnv(
        #         [compute_dict['pd_1_1_d1'], compute_dict['pd_1_2_d1'], data_year['pd_2_d_t_gz']]
        #     )
        # ),
        # 'pd_6_p1_p_0_p1': compute_divided_parametr_3(
        #     *cnv(
        #         [compute_dict['pd_3_p1_fot_0_p_1'], compute_dict['pd_4_p1_vf_0_p_2'], data_year['pd_5_p1_p_pr_0_p_2']]
        #     )
        # ),
    }
    calculate_dict_1 = {
        'pfu_13': divided_12_percent(
            *cnv(
                [calculated_dict['pfu_12_oc_2'], data_21['p_p']]
            )
        ),

    }
    compute_dict.update(calculate_dict_1)
    compute_dict.update(calculated_dict)

    return compute_dict

def compute_all_fs_(data):
    data_20 = data['01012020']
    data_21 = data['01012021']
    # data_year = data['year']

    compute_dict = {
        "id": data["id"],

        'op_1_d_t_delta': average_percent(
            *cnv(
            [data_21['d_t'], data_20['d_t']]
            ), a='op_1_d_t_delta',

        ),
        'op_1a': average_percent(
            *cnv(
                [data_21['d_t_1'], data_20['d_t']]
            ), a='op_1_d_t_delta',

        ),
        # Start Oleg's code
        'op_2': average_percent(
            *cnv(
                [data_21['uz_t_vo'],data_20['uz_t_vo']]
            )
        ),
        'op_2a': average_percent(
            *cnv(
                [data_21['uz_t_vo_1'], data_21['uz_t']]
            )
        ),
        'op_3': average_percent(
            *cnv(
                [data_21['uz_t_spo'], data_20['uz_t_spo']]
            )
        ),
        'op_3a': average_percent(
            *cnv(
                [data_21['uz_t_spo_1'], data_21['uz_t_spo']]
            )
        ),
        'op_3a': average_percent(
            *cnv(
                [data_21['uz_t_spo_1'], data_21['uz_t_spo']]
            )
        ),
        'op_4_p_t_delta': average_percent(
            *cnv(
                [data_21['p_t'], data_20['p_t']]
            ),
            a='op_4_p_t_delta'
        ),
        'op_4a': average_percent(
            *cnv(
                [data_21['p_t_1'], data_20['p_t']]
            ),
            a='op_4_p_t_delta'
        ),
        # end Oleg's code
        'op_10_d_t_max_percent_20': max_percent(
            *cnv(
                [data_20['d_t_'], data_20['d_t_gz'], data_20['d_t_ic'], data_20['d_t_oms'], data_20['d_t_pdd']]
            )
        ),
        'op_10_d_t_max_percent_21': max_percent(
            *cnv(
                [data_21['d_t_'], data_21['d_t_gz'], data_21['d_t_ic'], data_21['d_t_oms'], data_21['d_t_pdd']]
            )
        ),
        'op_10a': max_percent(
            *cnv(
                [data_21['d_t_1'], data_21['d_t_gz_1'], data_21['d_t_ic_1'], data_21['d_t_oms_1'], data_21['d_t_pdd_1']]
            )
        ),
        'op_5': average_percent(
            *cnv(
                [data_21['fot_t'], data_20['fot_t']]
            ),
            a='op_5'
        ),
        'op_5a': average_percent(
            *cnv(
                [data_21['fot_t_1'], data_20['fot_t']]
            ),
            a='op_5'
        ),
        'op_6': compute_1(
            *cnv(
                [data_21['os_t_ng'], data_21['d_t'], data_21['p_t']]  # Oleg - change:  data_20['p_t']] →  data_21['p_t']]
            )
        ),
        'op_6a': compute_1(
            *cnv(
                [data_21['os_t_ng_1'], data_21['d_t_1'], data_21['p_t_1']]
                # Oleg - change:  data_20['p_t']] →  data_21['p_t']]
            )
        ),
        'op_7': divided_two_minus_percent(
            *cnv(
                [data_21['d_t'], data_21['p_t']]
            )
        ),
        'op_7a': divided_two_minus_percent(
            *cnv(
                [data_21['d_t_1'], data_21['p_t_1']]
            )
        ),

        'op_9': sum_6_abs_percent(
            *cnv(
                [data_21['os_t_pdd'], data_21['d_t_pdd'], data_21['p_t_pdd'], data_21['z_t_uv'], data_21['z_t_um']]
            )
        ),
        'op_9a': sum_6_abs_percent(
            *cnv(
                [data_21['os_t_pdd_1'], data_21['d_t_pdd_1'], data_21['p_t_pdd_1'], data_21['z_t_uv_1'], data_21['z_t_um_1']]
            )
        ),
        'pfu_3': divided_2_percent(
            *cnv(
                [data_21['d_t_o'], data_21.get('d_t_pdd')]
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
                [data_21['kz_pros'], data_21['kz']] # Oleg - change:  data_21['kz_pr'] → data_21['kz_pros'],
                # data_21['kz_t']] → data_21['kz']]
            )
        ),
        'pfu_5': divided_2_percent(
            *cnv(
                [data_21['dz_pros'], data_21['dz']]# Oleg - change:  data_21['dz_t'] → data_21['dz'],
            )
        ),
        'pfu_7': sum_2_parametr_percent(
            *cnv(
                [data_21['d_t_o'], data_21['kz'], data_21['d_t_']]# Oleg - change:  data_21['d_t'] → data_21['d_t_'],
                # data_21['kz_t']] → data_21['kz']]
            )
        ),
        'pfu_8': sum_2_parametr_percent(
            *cnv(
                [data_21['dz_z'], data_21['dz'], data_21['vb_t']]
                # data_21['dz_t']] → data_21['dz']]
            )
        ),
        'pfu_9': sum_2_parametr_percent(
            *cnv(
                [data_21['dz_z'], data_21['dz'], data_21['d_t_']]# Oleg - change:  data_21['d_t'] → data_21['d_t_'],
                # data_21['dz_t']] → data_21['dz']]
            )
        ),

        # 'pfu_11': divided_12_percent(
        #     *cnv(
        #         [data_21['os_1'], data_21['rp']]  # Oleg - change:  data_21['d_t'] → data_21['d_t_'],
        #         # data_21['dz_t']] → data_21['dz']]
        #     )
        # ),
        # 'pfu_12': diffence(
        #     *cnv(
        #         [data_21['os_2'], data_21['rp']]  # Oleg - change:  data_21['d_t'] → data_21['d_t_'],
        #         # data_21['dz_t']] → data_21['dz']]
        #     )
        # ),
        # 'pfu_13': divided_12_percent(
        #     *cnv(
        #         [data_21['os_1'], data_21['kz_pr']]  # Oleg - change:  data_21['d_t'] → data_21['d_t_'],
        #         # data_21['dz_t']] → data_21['dz']]
        #     )
        # ),
        'pfu_10_oc_1': compute_average_percent(
            *cnv(
                [data_21['os'], data_21['kz_zpvf']]
            )
        ),
        'pfu_14': divided_12_parametr_3_percent(
            *cnv(
                [data_21['kz_zpvf'], data_21['fot_p'], data_21['k_zp']]# Oleg - change:  data_21['kz_zp'] → data_21['kz_zpvf'],
            )
        ),
        'pfu_15': divided_12_coef_parametr_3_percent(
            *cnv(
                [data_21['kz_vf'], data_21['fot_p'], data_21['k_vf']]
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
        'lp_3_ko_delta': difference_abs(
            *cnv(
                [data_21['z_1_pdd'], data_21['z_2_pdd']]
            )
        ),
        # 'pd_1_1_d1': difference_abs(
        #     *cnv(
        #         [data_21['d_tf_pdd'], data_year['pd_1_d_t_pdd'],data_21['d_tp_pdd']]
        #     )
        # ),
        # 'pd_1_2_d1': difference_abs(
        #     *cnv(
        #         [data_21['d_tf_oms'], data_year['pd_1_2_d_t_oms'], data_21['d_tp_oms']]
        #     )
        # ),
        # # TODO:// что с регистром диктов
        # 'pd_3_p1_fot_0_p_1': divided_difference_parametr_4(
        #     *cnv(
        #         [data_21['fot_tf'], data_20['fot_tf'], data_year['fot_tp'], data_year['fot_tf']]
        #     )
        # ),
        # # TODO:// что с регистром диктов
        # 'pd_4_p1_vf_0_p_2': divided_difference_parametr_4(
        #     *cnv(
        #         [data_21['vf_tf'], data_20['vf_tf'], data_year['vf_tp'], data_year['vf_tf']]
        #     )
        # ),
        # 'pd_5_p1_p_pr_0_p_2': divided_difference_parametr_4(
        #     *cnv(
        #         [data_21['p_tf'], data_20['vp_tf'], data_year['p_tp'], data_year['p_tf']]
        #     )
        # ),

    }
    # 88 стр
    calculated_dict = {
        'op_3_d_t_max_delta_max_percent': average_percent(
            *cnv(
                [compute_dict['op_2_d_t_max_value_21'], compute_dict['op_2_d_t_max_value_20']]
                # Oleg's change: [compute_dict['op_2_d_t_max_percent_21'], compute_dict['op_2_d_t_max_percent_20']] →
                # → [compute_dict['op_2_d_t_max_value_21'], compute_dict['op_2_d_t_max_value_20']]
            ),
           a='op_3_d_t_max_delta_max_percent'
        ),
        'op_8': compute_average_percent(
            *cnv(
                [compute_dict['op_4_p_t_delta'], compute_dict['op_1_d_t_delta']]
            )
        ),
        'op_8a': compute_average_percent(
            *cnv(
                [compute_dict['op_4a'], compute_dict['op_1a']]
            )
        ),
        'pfu_11': divided_12_percent(
            *cnv(
                [compute_dict['pfu_10_oc_1'], data_21['p_p']]
            )
        ),
        'pfu_11a': divided_12_percent(
            *cnv(
                [compute_dict['pfu_10_oc_1'], data_21['p_p']]
            )
        ),
        'pfu_12_oc_2': compute_average_percent(
            *cnv(
                [compute_dict['pfu_10_oc_1'], compute_dict['kz_pr']]
            )
        ),
        'lp_4': divided_2_percent(
            *cnv(
                [compute_dict['lp_3_ko_delta'], data_21['d_pt_pdd']]
            )
        ),
        'lp_5': sum_2_parametr_percent(
            *cnv(
                [data_21.get('d_t_o',0), compute_dict['lp_3_ko_delta'], data_21['d_pt_pdd']]
            )
        ),
        # 'pd_2_d1': compute_divided_parametr_3(
        #     *cnv(
        #         [compute_dict['pd_1_1_d1'], compute_dict['pd_1_2_d1'], data_year['pd_2_d_t_gz']]
        #     )
        # ),
        # 'pd_6_p1_p_0_p1': compute_divided_parametr_3(
        #     *cnv(
        #         [compute_dict['pd_3_p1_fot_0_p_1'], compute_dict['pd_4_p1_vf_0_p_2'], data_year['pd_5_p1_p_pr_0_p_2']]
        #     )
        # ),
    }
    calculate_dict_1 = {
        'pfu_13': divided_12_percent(
            *cnv(
                [calculated_dict['pfu_12_oc_2'], data_21['p_p']]
            )
        ),

    }
    compute_dict.update(calculate_dict_1)
    compute_dict.update(calculated_dict)

    return compute_dict

def compute_score(d):
    res = {
    "op_1_score": score_op_1(d["op_1_d_t_delta"]),
    "op_2_score": score_op_2_3(d["op_2_d_t_max_value_21"]),
    "op_5_score": score_op_5(d["op_5"]),
    "op_7_score": score_op_7(d["op_7"]),
    "op_8_score": score_op_8(d["op_8"]),
    "pfu_3_score": score_pfu_3(d["pfu_3"]),
    "pfu_6_score": score_pfu_6(d["pfu_6"]),
    "pfu_10_score": score_pfu_10(d["pfu_11"],d["pfu_10_oc_1"]),
    "pfu_12_score": score_pfu_12(d["pfu_13"],d["pfu_12_oc_2"]),
    "pfu_14_score": score_pfu_14_15(d["pfu_14"]),
    "pfu_15_score": score_pfu_14_15(d["pfu_15"]),
    "lp_3_score": score_lp_3(d["lp_3_ko_delta"]),
    "lp_5_score": score_lp_5(d["lp_5"]),
    }
    res_1 = {
        "v_1_score" : sum([res["op_1_score"],res["op_5_score"],res["op_7_score"],res["pfu_3_score"],res["pfu_6_score"]]), # Oleg's change: delete ,res["op_2_score"]
        "v_2_score" : sum([res["op_1_score"],res["op_5_score"],res["op_7_score"],res["op_8_score"],res["pfu_3_score"],res["pfu_6_score"]]), # Oleg's change: delete ,res["op_2_score"]
        "v_3_score": sum([res["pfu_10_score"],res["pfu_12_score"],res["pfu_14_score"],res["pfu_15_score"],res["lp_3_score"], res['lp_5_score'] ])
    }
    res.update(res_1)
    return res