from collections import deque
from sys import maxsize


def word_conversion(begin, target, words):
    """
    프로그래머스 코딩테스트 고득점 Kit
    DFS BFS: 단어 변환 솔루션

    Author: Oh Donggeon
    Date: 2022/03/31
    link: https://programmers.co.kr/learn/courses/30/lessons/43163

    :param begin: 시작 단어
    :param target: 목표 단어
    :param words: 시작 단어에서 변환 할 수 있는 단어 배열
    :return: 목표 단어까지 변환하는 최소 횟수
    """
    queue = deque()
    answer = maxsize

    queue.appendleft((begin, set(words.copy()), 0))

    while queue:
        cur_word, remain_words, count = queue.pop()

        if cur_word == target:
            answer = count if count < answer else answer
            continue

        for word in remain_words:
            diff_count = 0

            for cur_word_char, word_char in zip(cur_word, word):
                if cur_word_char != word_char:
                    diff_count += 1

            if diff_count == 1:
                next_words = remain_words.copy()
                next_words.remove(word)

                queue.appendleft((word, next_words, count + 1))

    return 0 if answer == maxsize else answer
