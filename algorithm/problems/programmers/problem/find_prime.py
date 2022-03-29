from itertools import permutations
from functools import reduce


def find_prime(numbers):
    """
    프로그래머스 코딩테스트 고득점 Kit 완전탐색 - 소수 찾기 솔루션

    Author: Oh Donggeon
    Date: 2022/03/29
    Link: https://programmers.co.kr/learn/courses/30/lessons/42839

    :param numbers: 숫자의 배열
    :return: numbers로 조합할 수 있는 모든 수에서 소수인 숫자의 갯수
    """
    prime_set = set()

    for select_number in range(1, len(numbers) + 1):
        for prime_numbers in set(permutations(numbers, select_number)):
            prime_number = int(reduce(lambda lhs, rhs: lhs + str(rhs), prime_numbers, ''))

            if is_prime(prime_number):
                prime_set.add(prime_number)

    return len(prime_set)


def is_prime(number):
    if number == 0 or number == 1:
        return False

    elif number == 2:
        return True

    elif number % 2 == 0:
        return False

    for mod_operand in range(3, number // 2, 2):
        if number % mod_operand == 0:
            return False

    return True
