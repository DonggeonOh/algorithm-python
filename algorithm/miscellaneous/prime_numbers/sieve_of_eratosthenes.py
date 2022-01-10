from math import sqrt


def sieve_of_eratosthenes(num):
    """
    에라토스테네스의 체 알고리즘은 특정 안에 존재하는 모든 소수를 찾을 때 유용하다.
    set을 이용하여 작성한 코드이다.

    :param num: 2부터 num 범위의 소수를 판별
    :return: 2부터 num 까지의 소수를 반환
    """
    prime_list = set([number for number in range(2, num + 1)])

    for i in range(2, int(sqrt(num)) + 1):
        if i in prime_list:
            multi = i

            while multi <= num:
                multi += i
                prime_list.discard(multi)

    return prime_list
