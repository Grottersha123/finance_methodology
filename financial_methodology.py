def average_percent(*args):
    return round(args[0] / args[1] * 100 - 100, 4)


def max_percent(*args):
    return round(max([args[1] / args[0], args[2] / args[0], args[3] / args[0], args[4] / args[0]]) * 100, 4)


def compute_1(*args):
    return round(args[0] + args[1] - args[2], 4)


def divided_two_minus_percent(*args):
    return round((args[0]-args[1]) / args[0],4)

def compute_average_percent(*args):
    return args[0] - args[1]


def sum_6_abs_percent(*args):
    return (args[0] + args[1] - args[2] + args[3] - abs(args[4])) / args[1] * 100


def divided_2_percent(*args):
    return args[0] / args[1] * 100


def sum_3_abs_percent(*args):
    return (args[0] + args[1] - abs(args[2])) / args[3] * 100


def sum_3_percent(*args):
    return (args[0] + args[1] - args[2]) / args[3] * 100


def diffence(*args):
    return args[0] - args[1]


# не ясно что с делителем
def divided_12_percent(*args):
    return args[0] / (args[1] / 12) * 100


# не ясно с делителем
def divided_12_parametr_3_percent(*args):
    return args[0] / (args[1] / (12 * args[2])) * 100


def divided_12_coef_parametr_3_percent(*args):
    return args[0] / (args[1] / (12 * args[2] * 0.302)) * 100


def sum_2_parametr_percent(*args):
    return ((args[0] + args[1]) / args[3]) * 100


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
    return args[0] + divided_parametr_3(*args[1]) + divided_parametr_3(*args[2])


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
