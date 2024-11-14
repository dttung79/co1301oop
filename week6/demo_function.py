def add(a, b):
    c = a + b
    return c


def get_rank(score):
    if type(score) != int:
        return 'Invalid'
    if score < 0 or score > 100:
        return 'Invalid'
    if score < 40:
        return 'Fail'
    elif score < 60:
        return 'Pass'
    elif score <= 80:
        return 'Merit'
    else:
        return 'Distinction'