from itertools import combinations
import sys


def blackjack(score, cards):
    """
    백준 2798번 블랙잭 솔루션 - 조합

    @Date: 2022/03/25
    @Author: Oh Donggeon
    @Link: https://www.acmicpc.net/problem/2798

    :param score: 목표 스코어
    :param cards: 카드의 숫자 배열
    :return: 3개의 카드를 뽑은 후 더한 값이 score에 가장 근접한 숫자
    """
    comb_cards = combinations(cards, 3)
    result = 0

    for comb_card in comb_cards:
        target = 0

        for element in comb_card:
            target += element

        if target <= score:
            result = max(result, target)

    return result


def blackjack_recur(score, cards):
    """
    백준 2798번 블랙잭 솔루션 - 재귀

    @Date: 2022/03/25
    @Author: Oh Donggeon
    @Link: https://www.acmicpc.net/problem/2798

    :param score: 목표 스코어
    :param cards: 카드의 숫자 배열
    :return: 3개의 카드를 뽑은 후 더한 값이 score에 가장 근접한 숫자
    """
    visited = [False for _ in range(0, len(cards))]

    return blackjack_recursive(score, 0, 0, 0, cards, visited)


def blackjack_recursive(score, cur_score, selected_cards, start, cards, visited):
    if selected_cards > 3:
        return cur_score

    result = cur_score

    for index in range(start, len(cards)):
        next_score = cur_score + cards[index]

        if not visited[index] and next_score <= score:
            visited[index] = True
            result = max(blackjack_recursive(score, next_score, selected_cards + 1, start + 1, cards, visited), result)

        visited[index] = False

    return result


num, score = map(int, sys.stdin.readline().split())
cards = list(map(int, sys.stdin.readline().split()))

print(blackjack(score, cards))
