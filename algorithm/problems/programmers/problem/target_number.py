from collections import deque


def target_number(numbers, target):
    """
    프로그래머스 코딩테스트 고득점 Kit
    완전탐색: 타겟 넘버 솔루션

    Author: Oh Donggeon
    Date: 2022/04/01
    Link: https://programmers.co.kr/learn/courses/30/lessons/43165

    :param numbers: 숫자 배열
    :param target: 결과 값
    :return: 숫자들의 덧셈 뺄셈 조합을 통해
    """
    queue = deque()
    answer = 0

    queue.appendleft((0, 0))

    while queue:
        number, index = queue.pop()

        if index == len(numbers):
            if number == target:
                answer += 1
            continue

        queue.appendleft((number + numbers[index], index + 1))
        queue.appendleft((number - numbers[index], index + 1))

    return answer
