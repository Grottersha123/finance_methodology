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
    if a >=10 and a < 15:
        return 0.75
    if a >=15 and a < 50:
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
    if a > -15:
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

def score_pfu_10(a,b):
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

def score_pfu_12(a,b):
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
    if a >=100:
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