from math import sqrt


def primality(n):
    prime_str = "Prime"
    not_prime_str = "Not prime"

    if n == 1:
        return not_prime_str
    elif n % 2 == 0 and n != 2:
        return not_prime_str

    for num in range(3, int(sqrt(n) + 1), 2):
        if n % num == 0 and n != num:
            return not_prime_str

    return prime_str
