def super_digit(digit, iteration):
    digit = str(add_digit_eval(digit) * iteration)

    while len(digit) != 1:
        digit = str(add_digit_eval(digit))

    return digit


def add_digit_eval(digit):
    return eval("+".join(digit))
