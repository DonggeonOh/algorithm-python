def super_digit(digit, iteration):
    """
    해커랭크 Recursive Digit Sum 솔루션
    """
    digit = str(eval("+".join(digit)) * iteration)

    while len(digit) != 1:
        temp_list = list()

        for number in digit:
            add_digit_list(temp_list, int(number))

        digit = "".join([str(element) for element in reversed(temp_list)])

    return digit


def add_digit_list(digit_list, digit):
    if not digit_list:
        digit_list.append(digit)
        return

    for index, element in enumerate(digit_list):
        if element + digit > 10:
            target = divmod(element + digit, 10)
            digit_list[index] = target[1]
            digit = target[0]

        else:
            digit_list[index] += digit
            digit = 0
            break

    if digit:
        digit_list.append(digit)
