from financial_methodology import average_percent, max_value, diffence, max_percent, compute_1, \
    divided_two_minus_percent, sum_6_abs_percent, \
    divided_2_percent, sum_3_abs_percent, sum_3_percent, compute_average_percent, divided_12_parametr_3_percent, \
    divided_12_coef_parametr_3_percent, sum_2_parametr_percent, difference_abs, divided_12_percent, \
    average_percent_rfkm, average_percent_minus_rfkm, average_percent_two_rfkm, average_percent_6_12_rfkm, sp_1_rfkm, \
    average_percent_3_rfkm, average_percent_fot_rfkm, sp_1_rfkm_on, divided_4_percent
from score_op import score_op_1, score_op_2_3, score_op_5, score_op_7, score_op_8, score_pfu_3, score_pfu_6, \
    score_pfu_10, score_pfu_12, score_pfu_14_15, score_lp_3, score_lp_5, score_pkp_3, score_pkp_2, score_sp_7, \
    score_pkp_1, score_pfu_1, score_pfu_2, score_pfu_5, score_pfu_7, score_sp_1, score_sp_3, score_sp_2, score_sp_4, \
    score_sp_5, score_sp_6

def convert_none(lst):
    return [0 if v is None else v for v in lst]

def cnv(lst):
    try:
        return list(map(float, convert_none(lst)))
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

def compute_all_fs(data):
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


def compute_all_rkfm_oovo(data):
    d_1 = data['01012021']
    compute_dict = {
        'pkp_1': average_percent_rfkm(
            *cnv(
                [d_1['d_f'], d_1['d_p']]
            )
        ),
        'pkp_2': average_percent_rfkm(
            *cnv(
                [d_1['p_f'], d_1['p_p']]
            )
        ),
        'pkp_3': average_percent_minus_rfkm(
            *cnv(
                [d_1['o_s'], d_1['o_bt'],d_1['o_bs'],d_1['p_as'],d_1['d_gz'] ]
            )
        ),
        'pfu_1': average_percent_two_rfkm(
            *cnv(
                [d_1['d_pdd '], d_1['d_gz']]
            )
        ),
        'pfu_2': average_percent_6_12_rfkm(
            *cnv(
                [d_1['kz_fot'], d_1['kz_n'], d_1['kz_kucn'],d_1['p_fot_vf'],d_1['p_n'], d_1['p_kucn']]
            )
        ),
        'pfu_3': divided_2_percent(
            *cnv(
                [d_1['d_o'], d_1['d_pdd']]
            )
        ),
        'pfu_4': divided_2_percent(
            *cnv(
                [d_1['kz_pros'], d_1['kz']]
            )
        ),
        'pfu_5': divided_2_percent(
            *cnv(
                [d_1['dz_pros'], d_1['dz']]
            )
        ),
        'pfu_6': divided_2_percent(
            *cnv(
                [d_1['os_pdd'], d_1['p_fotvf'],d_1['p_n'],d_1['p_ku'],d_1['d_pdd']]
            )
        ),
        'sp_1': sp_1_rfkm(
            *cnv(
                [d_1['fnz_t_pps'], d_1['cch_t_pps'], d_1['t'], d_1['zp_t_sr']]
            )
        ),
        'sp_3': divided_2_percent(
            *cnv(
                [d_1['p_fotvf'], d_1['p']]
            )
        ),
        'sp_4': divided_2_percent(
            *cnv(
                [d_1['fnz_op'], d_1['fnz_obs']]
            )
        ),
    }

def check_keys_in_json_rkfm_no(data_dict):
    parametrs = ['d_f','d_p',
                 'r_f','r_p',
                 'o_s','o_bt','o_bs','p_ac','d_gz',
                 'd_t_pdd','d_t_oms','d_t_z',
                 'd_o','d_pdd',
                 'kz_pros','kz',
                 'dz_pros','dz',
                 'vla','dz','kz','d_pdd_f',
                 'kz_fot', 'kz_vf','kz_n','kz_ku','fot','r_n','r_ku',
                 's_vnsh', 's_obsh',
                 'fnz_t_ns','ssch_t_ns','zp_t_sr',
                 'p_fotvf', 'p',
                 'fnz_op', 'fnz_obs','ssch_t_np39','ssch_t_np',
                 'rid_t',
                 'niokr_pdd','niokr_gz',
                 'd_niokr', 'op',
                 'fr_rid','rid_s'
                 ]
    d_1 = data_dict['01012021']
    d_0 = data_dict['01012020']
    for p in parametrs:
        if p not in d_1.keys():
            data_dict['01012021'].update({
                p : 0
            })
            print('missing', p)
        if p not in d_0.keys():
            data_dict['01012020'].update({
                p: 0
            })
    return data_dict

def compute_all_rkfm_no(data,id_=''):
    data = check_keys_in_json_rkfm_no(data)
    d_1 = data['01012021']
    d_0 = data['01012020']
    compute_dict = {
        'pkp_1': average_percent_rfkm(
            *cnv(
                [d_1['d_f'], d_1['d_p']]
            )
        ),
        'pkp_2': average_percent_rfkm(
            *cnv(
                [d_1['r_f'], d_1['r_p']]
            )
        ),
        'pkp_3': average_percent_minus_rfkm(
            *cnv(
                [d_1['o_s'], d_1['o_bt'], d_1['o_bs'], d_1['p_ac'], d_1['d_gz'] ]
            )
        ),
        'pfu_1': average_percent_3_rfkm(
            *cnv(
                [d_1['d_t_pdd'], d_1['d_t_oms'], d_1['d_t_z']]
            )
        ),
        'pfu_2': divided_2_percent(
            *cnv(
                [d_1['d_o'], d_1['d_pdd']]
            )
        ),
        'pfu_3': divided_2_percent(
            *cnv(
                [d_1['kz_pros'], d_1['kz']]
            )
        ),
        'pfu_4': divided_2_percent(
            *cnv(
                [d_1['dz_pros'], d_1['dz']]
            )
        ),
        'pfu_5': sum_3_percent(
            *cnv(
                [d_1['vla'], d_1['dz'],d_1['kz'], d_1['d_pdd_f']]
            )
        ),
        'pfu_6': average_percent_fot_rfkm(
            *cnv(
                [d_1['kz_fot'], d_1['kz_vf'], d_1['kz_n'], d_1['kz_ku'],d_1['fot'], d_1['r_n'], d_1['r_ku']]
            )
        ),
        'pfu_7': divided_2_percent(
            *cnv(
                [d_1['s_vnsh'], d_1['s_obsh']]
            )
        ),
        'sp_1': sp_1_rfkm_on(
            *cnv(
                [d_1['fnz_t_ns'], d_1['ssch_t_ns'], d_1['zp_t_sr']]
            )
        ),
        # не понятно
        # 'sp_2': sp_1_rfkm_on(
        #     *cnv(
        #         [d_1['fnz_t_ns'], d_1['ssch_t_ns '], d_1['zp_t_sr']]
        #     )
        # ),
        'sp_2': 0,
        'sp_3': divided_2_percent(
            *cnv(
                [d_1['p_fotvf'], d_1['p']]
            )
        ),
        'sp_4': divided_2_percent(
            *cnv(
                [d_1['fnz_op'], d_1['fnz_obs']]
            )
        ),
        'sp_5': divided_4_percent(
            *cnv(
                [d_1['ssch_t_np39'], d_1['ssch_t_np'], d_0['ssch_t_np39'], d_0['ssch_t_np']]
            )
        ),
        'sp_6': diffence(
            *cnv(
                [d_1['rid_t'], d_0['rid_t']]
            )
        ),
        'sp_7': divided_2_percent(
            *cnv(
                [d_1['niokr_pdd'], d_0['niokr_gz']]
            )
        ),
        'dp_1': divided_2_percent(
            *cnv(
                [d_1['d_niokr'], 100*d_0['op']]
            )
        ),
        'dp_2': divided_2_percent(
            *cnv(
                [d_1['fr_rid'], d_0['rid_s']]
            )
        ),
        'id':id_
    }
    return compute_dict

def compute_score_rkfm_no(d):
    res = {
    "pkp_1_score":score_pkp_1(d["pkp_1"]),
    "pkp_2_score":score_pkp_2(d["pkp_2"]),
    "pkp_3_score":score_pkp_3(d["pkp_3"]),
    "pfu_1_score":score_pfu_1(d["pfu_1"]),
    "pfu_2_score":score_pfu_2(d["pfu_2"]),
    "pfu_3_score":score_pfu_3(d["pfu_3"]),
    "pfu_5_score":score_pfu_5(d["pfu_5"]),
    "pfu_6_score":score_pfu_6(d["pfu_6"]),
    "pfu_7_score":score_pfu_7(d["pfu_7"]),
    "sp_1_score": score_sp_1(d["sp_1"]),
    "sp_2_score": score_sp_2(d["sp_2"]),
    "sp_3_score": score_sp_3(d["sp_3"]),
    "sp_4_score": score_sp_4(d["sp_4"]),
    "sp_5_score": score_sp_5(d["sp_5"]),
    "sp_6_score": score_sp_6(d["sp_6"]),
    "sp_7_score": score_sp_7(d["sp_7"]),
    }
    return res

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
