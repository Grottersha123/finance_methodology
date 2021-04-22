def score_op_1(a):
    if a <= -50:
        return 1.25
    if -50 <= a < -15:
        return 1
    if -15 <= a < -10:
        return 0.75
    if -10 <= a:
        return 0


def score_op_2_3(a):
    if a >= 10 and a < 15:
        return 0.75
    if a >= 15 and a < 50:
        return 1.0
    if a > 50:
        return 1
    else:
        return 0.75


def score_op_5(a):
    if a <= -30:
        return 1.25
    if -30 <= a <= -15:
        return 1.25
    if -15 < a:
        return 0


def score_op_7(a):
    if a >= 10 and a < 50:
        return 1.0
    if a >= 50:
        return 1.25
    else:
        return 0


def score_op_8(a):
    if a >= 15:
        return 1.0
    else:
        return 0


def score_pfu_3(a):
    if a >= 25:
        return 1.0
    if a > 10 and a < 15:
        return 0.5
    if a > 50:
        return 0.75
    else:
        return 0


def score_pfu_6(a):
    if a >= 15:
        return 1.0
    else:
        return 0


def score_pfu_10(a, b):
    if a <= 10:
        return 0.5
    elif b <= 0:
        return 1
    if a <= -100:
        return 1.25
    if a <= -200:
        return 1.5
    else:
        return 0


def score_pfu_12(a, b):
    if a <= 10:
        return 0.5
    if b <= 0:
        return 1
    if a <= -100:
        return 1.25
    if a <= -200:
        return 1.5
    else:
        return 0


def score_pfu_14_15(a):
    if a >= 100:
        return 0.25
    if a >= 125:
        return 1.25
    if a >= 200:
        return 1.5
    else:
        return 0


def score_lp_3(a):
    if a >= 0:
        return 0.5
    else:
        return 0


def score_lp_5(a):
    if a >= 25:
        return 1
    else:
        return 0


def score_pkp_1(a):
    if a < 90:
        return 0
    if 95 < a < 90:
        return 0.5
    else:
        return 1


def score_pkp_1(a):
    if a < 90 or a == 'Null':
        return 0
    if 95 < a < 90:
        return 0.5
    if a == 'Null':
        return 'Null'
    else:
        return 1


def score_pkp_2(a):
    if a < 90:
        return 0
    if 97 < a < 90:
        return 0.5
    if a == 'Null':
        return 'Null'
    else:
        return 1


def score_pkp_3(a):
    if a < 0:
        return 1
    if 0 < a < 4:
        return 0.5
    if a == 'Null':
        return 'Null'
    else:
        return 1


def score_pfu_1(a):
    if a <= 15:
        return 0
    if 15 < a < 30:
        return 1
    if a > 30:
        return 1
    if a == 'Null':
        return 'Null'


def score_pfu_2(a):
    if 0 <= a <= 10:
        return 1
    if 10 < a < 25:
        return 0.5
    if a > 25:
        return 0
    if a == 'Null':
        return 'Null'


def score_pfu_3(a):
    if a <= 0:
        return 1
    if 0 < a < 1:
        return 0.5
    if a > 1:
        return 0
    if a == 'Null':
        return 'Null'


def score_pfu_4(a):
    if a <= 0:
        return 1
    if 0 < a < 1:
        return 0.5
    if a > 1:
        return 0
    if a == 'Null':
        return 'Null'



def score_pfu_5(a):
    if a <= 15:
        return 1
    if 15 < a < 0:
        return 0.5
    if a > 0:
        return 1
    if a == 'Null':
        return 'Null'

def score_pfu_6(a):
    if a <= 100:
        return 1
    if a == 'Null':
        return 'Null'
    else:
        return 0



def score_pfu_7(a):
    if a >= 30:
        return 0
    if 15 < a < 30:
        return 0.5
    if a < 15:
        return 1
    if a == 'Null':
        return 'Null'


def score_sp_1(a):
    if a <= 185:
        return 0
    if 185 < a < 200:
        return 0.5
    if a > 200:
        return 1
    if a == 'Null':
        return 'Null'


def score_sp_2(a):
    if a <= 185:
        return 0
    if 185 < a < 200:
        return 0.5
    if a > 200:
        return 1
    if a == 'Null':
        return 'Null'

def score_sp_2a(a):
    if a <= 0:
        return 0
    if a > 0:
        return 1
    if a == 'Null':
        return 'Null'

def score_sp_3(a):
    if a <= 80:
        return 1
    if a > 80:
        return 0
    if a == 'Null':
        return 'Null'


def score_sp_4(a):
    if a <= 60:
        return 0
    if a > 60:
        return 1
    if a == 'Null':
        return 'Null'


def score_sp_5(a):
    if a <= 2:
        return 0
    if -2 < a < 2:
        return 0.5
    if a > 2:
        return 1
    if a == 'Null':
        return 'Null'

def score_sp_6(a):
    if a <= -2:
        return 0
    if -2 < a < 2:
        return 0.5
    if a > 2:
        return 1
    if a == 'Null':
        return 'Null'


def score_sp_7(a):
    if a <= 10:
        return 0
    if 10 < a < 15:
        return 0.5
    if a > 15:
        return 1
    if a == 'Null':
        return 'Null'



def pkp_1_score(a):
    if a == 'Null':
        return 'Null'
    if a >= 90:
        return 1
    if 90 < a < 95:
        return 0.5
    if a <= 90:
        return 0

def pkp_2_score(a):
    if a == 'Null':
        return 'Null'
    if a >= 97:
        return 1
    if 90 < a < 97:
        return 0.5
    if a <= 90:
        return 0

# TODO новая методичка
def pkp_3_score(a):
    if a == 'Null':
        return 'Null'
    if a >= 92:
        return 0
    if 92 < a < 99:
        return 0.5
    if a <= 97:
        return 1

# TODO:/ новое
def pkp_4_score(a):
    if a == 'Null':
        return 'Null'
    if 25 < a < 35:
        return 0.5
    if 0 < a > 25:
        return 1
    if 0 < a > 35:
        return 0

    else:
        return 0

def pkp_5_score(a):
    if a == 'Null':
        return 'Null'
    if a >= 4:
        return 1
    if 0 < a < 4:
        return 0.5
    if a <= 0:
        return 0


def pfu_1_score(a):
    if a == 'Null':
        return 'Null'
    if a >= 50:
        return 1
    if 30 < a < 50:
        return 0.5
    if a <= 30:
        return 0

def pfu_2_score(a):
    if a == 'Null':
        return 'Null'
    if a >= 100:
        return 0
    if a <= 100:
        return 1

def pfu_3_score(a):
    if a >= 25:
        return 0
    if 10 < a < 25:
        return 0.5
    if 0 <= a <= 10:
        return 1
    if a == 'Null':
        return 'Null'
def pfu_4_score(a):
    if a > 1:
        return 0
    if 0 <= a <= 1:
        return 0.5
    if a < 0:
        return 1
    if a == 'Null':
        return 'Null'
def pfu_5_score(a):
    if a > 5:
        return 0
    if 3 <= a <= 5:
        return 0.5
    if a < 3:
        return 1
    if a == 'Null':
        return 'Null'
def pfu_6_score(a):
    if a >= 0:
        return 1
    if -15 < a < 0:
        return 0.5
    if a <= -15:
        return 0
    if a == 'Null':
        return 'Null'
def sp_1_score(a):
    if a >= 200:
        return 1
    if 195 < a < 200:
        return 0.5
    if a <= 195:
        return 0
    if a == 'Null':
        return 'Null'
def sp_1a_score(a):
    if a >= 200:
        return 1
    if 195 < a < 200:
        return 0.5
    if a <= 195:
        return 0
    if a == 'Null':
        return 'Null'
def sp_2_score(a):
    if a >= 200:
        return 1
    if 195 < a < 200:
        return 0.5
    if a <= 195:
        return 0
    if a == 'Null':
        return 'Null'
def sp_2a_score(a):
    if a >= 0:
        return 1
    if a < 0:
        return 0
    if a == 'Null':
        return 'Null'
def sp_3_score(a):
    if a >= 80:
        return 0
    if 75 < a < 80:
        return 0.5
    if a < 75:
        return 1
    if a == 'Null':
        return 'Null'
def sp_4_score(a):
    if a >= 60:
        return 1
    if 55 < a < 60:
        return 0.5
    if a < 55:
        return 0
    if a == 'Null':
        return 'Null'
def pknpa_1_score(a):
    if a >= 0.75:
        return 1
    if a < 0.75:
        return 0
    if a == 'Null':
        return 'Null'
def pknpa_2_score(a):
    if a >= 0.75:
        return 1
    if a < 0.75:
        return 0
    if a == 'Null':
        return 'Null'
def pknpa_3_score(a):
    if a >= 0.75:
        return 1
    if a < 0.75:
        return 0
    if a == 'Null':
        return 'Null'
def dp_1_score(a):
    if a >= 0.75:
        return 1
    if a < 0.75:
        return 0
    if a == 'Null':
        return 'Null'