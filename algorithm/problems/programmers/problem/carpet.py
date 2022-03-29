from math import ceil


def carpet(brown, yellow):
    """
    프로그래머스 코딩테스트 고득점 Kit
    완전탐색: 카펫 솔루션

    Author: Oh Donggeon
    Date: 2022/03/29
    Link: https://programmers.co.kr/learn/courses/30/lessons/42842

    :param brown: 테두리의 카펫 갯수
    :param yellow: 중앙의 카펫 갯수
    :return: brown을 테두리로 하여 yellow를 품는 카펫의 가로, 세로를 배열에 담아 반환
    """
    yellow_divisor = get_divisor(yellow)
    yellow_length = len(yellow_divisor)

    for index in range(ceil(yellow_length / 2)):
        left_index = index
        right_index = yellow_length - index - 1

        row = get_length(yellow_divisor[left_index])
        col = get_length(yellow_divisor[right_index])

        if row * col == brown + yellow:
            return [max(row, col), min(row, col)]

    return [0, 0]


def get_divisor(number):
    result = list()

    for divisor_number in range(1, number + 1):
        if number % divisor_number == 0:
            result.append(divisor_number)

    return result


def get_length(number):
    return 3 if number == 1 else number + 2
