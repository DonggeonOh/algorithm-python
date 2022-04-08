import heapq


def scoville(scoville, K):
    """
    프로그래머스 코딩테스트 고득점 Kit
    힙(Heap): 더 맵게 솔루션

    Author: Oh Donggeon
    Date: 2022/04/08
    Link: https://programmers.co.kr/learn/courses/30/lessons/42626

    :param scoville: 스코빌 값이 담겨있는 배열
    :param K: 스코빌의 최솟값
    :return: K 이상의 스코빌을 가질수 있도록 하는 횟수
    """
    heapq.heapify(scoville)
    answer = 0

    while scoville:
        min_scoville = heapq.heappop(scoville)

        if min_scoville >= K:
            break

        elif not scoville:
            answer = -1
            break

        second_min_scoville = heapq.heappop(scoville)
        mixed_food_scoville = min_scoville + (second_min_scoville * 2)
        heapq.heappush(scoville, mixed_food_scoville)

        answer += 1

    return answer
