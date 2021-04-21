import logging

from icecream import ic


def average_percent(*args, a=''):
    try:
        return round((args[0] / args[1] * 100) - 100, 4)
    except Exception:
        ic('average_percent', a)
        return 0

def average_percent_rfkm(*args, a=''):
    try:
        return round(100 - ((args[0] - args[1]) / args[1] * 100), 4)
    except Exception:
        ic('average_percent_rfkm', args)
        return 'Null'


def average_percent_minus_rfkm(*args, a=''):
    try:
        return round((args[0]-args[1]-args[2]-args[3] / args[4]), 4)
    except Exception:
        ic('average_percent', a)
        return 0


def average_percent_two_rfkm(*args, a=''):
    try:
        return round((args[0] / (args[0] +args[1] )), 4)
    except Exception:
        ic('average_percent', a)
        return 0



def average_percent_3_rfkm(*args, a=''):
    try:
        return round(((args[0] + args[0] +args[1])/ (args[0] +args[1] + args[2] )), 4)
    except Exception:
        ic('average_percent', a)
        return 0


def average_percent_two_rfkm(*args, a=''):
    try:
        return round((args[0] / (args[0] +args[1] )), 4)
    except Exception:
        ic('average_percent', a)
        return 0


def average_percent_6_12_rfkm(*args, a=''):
    try:
        return round(((args[0] + args[1] + args[2]) / (args[3] + args[4] +  args[5])), 4)
    except Exception:
        ic('average_percent', a)
        return 0

def sp_1_rfkm(*args, a=''):
    try:
        return round(((args[0] / (args[0] + args[1] + args[2])), 4))
    except Exception:
        ic('average_percent', a)
        return 0

def sp_1_rfkm_on(*args, a=''):
    try:
        return round(((args[0] / (args[0] * args[1] * args[2])), 4))
    except Exception:
        ic('average_percent', a)
        return 0

#Start Oleg's code
def max_value(*args):
    return round(max([args[0], args[1], args[2], args[3]]), 4)
#end Oleg's code

def max_percent(*args):
    try:
        return round(max([args[1] / args[0], args[2] / args[0], args[3] / args[0], args[4] / args[0]]) * 100, 4)
    except ZeroDivisionError:
        ic('ZeroDivisionError', 'max_percent')
        return 0

def compute_1(*args):
    return round(args[0] + args[1] - args[2], 4)


def divided_two_minus_percent(*args):
    try:
        return round(((args[0]-args[1]) / args[0])*100,4)
    except ZeroDivisionError:
        logging.error('ZeroDivisionError', 'divided_two_minus_percent')
        return 0

def compute_average_percent(*args):
    return args[0] - args[1]


def sum_6_abs_percent(*args):
    try:
        return (args[0] + args[1] - args[2] + args[3] - abs(args[4])) / args[1] * 100
    except ZeroDivisionError:
        logging.error('ZeroDivisionError', 'sum_6_abs_percent')
        return 0

def divided_2_percent(*args):
    try:
        return args[0] / args[1] * 100
    except Exception as e:
        print(e, 'divided_2_percent')
        return 0


def divided_4_percent(*args):
    try:
        return (args[0] / args[1] -args[2] / args[3] ) * 100
    except Exception as e:
        print(e, 'divided_2_percent')
        return 0

def average_percent_fot_rfkm(*args, a=''):
    try:
        return round(((args[0] + args[1] + args[2] + args[3]) / (1.302 * args[4] + args[5] +  args[6])), 4)
    except Exception:
        ic('average_percent', a)
        return 0


def sum_3_abs_percent(*args):
    return (args[0] + args[1] - abs(args[2])) / args[3] * 100


def sum_3_percent(*args):
    try:

        return (args[0] + args[1] - args[2]) / args[3] * 100
    except Exception:
        ic('sum_3_percent', args)
        return 0


def diffence(*args):
    return args[0] - args[1]


# не ясно что с делителем
def divided_12_percent(*args):
    return args[0] / (args[1] / 12) * 100


# не ясно с делителем
def divided_12_parametr_3_percent(*args):
    return (args[0] / ((args[1] / 12) * args[2])) * 100


def divided_12_coef_parametr_3_percent(*args):
    return args[0] / ((args[1] / 12) * args[2] * 0.302) * 100


def sum_2_parametr_percent(*args):
    return ((args[0] + args[1]) / args[2]) * 100


def sum_12_parametr_3(*args):
    return ((args[0] - args[1]) / 12 * (5 + args[2]) + args[1]) / args[0] * 100


def sum_12_parametr_2(*args):
    return (((args[0] - args[1]) / 12) * 9 + args[1]) / args[0] * 100


def difference_abs(*args):
    return args[0] - abs(args[1])


def compute_difference_abs_percent(*args):
    return (args[0] + difference_abs(*args[1])) / args[2] * 100


def compute_difference_abs_parametr_2_percent(*args):
    return difference_abs(args[0]) / args[1] * 100


def divided_parametr_3(*args):
    return args[0] / args[2] * args[1]


def compute_divided_parametr_3(*args):
    return args[0] + args[1] + args[2]


def divided_difference_parametr_4(*args):
    return (args[0] - args[1]) / args[0] * args[2] + args[3]


def compute_divided_difference_parametr_4(*args):
    return divided_difference_parametr_4(*args[0]) + divided_difference_parametr_4(
        *args[1]) + divided_difference_parametr_4(*args[2])


def avr_parametr_3(*args):
    return (args[0] + args[1] - args[2]) / args[3]


def compute_avr_parametr_3(*args):
    return avr_parametr_3(*args[0]) * (12 - args[1]) + args[2] + args[3]


def compute_avr_parametr_3_coef(*args):
    return compute_avr_parametr_3(*args[0]) * (12 - args[1]) * 0.302 + args[2] + args[3]


# РР2
# о = ФОТР2
# о + ВФР2
# о + Рпр.Р2
# о
# ;uuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu
def compute_sum_avr_parametr_3_coef(*args):
    return compute_avr_parametr_3(*args[0]) + compute_avr_parametr_3_coef(*args[1]) + compute_avr_parametr_3(*args[2])


if __name__ == '__main__':
    pass
