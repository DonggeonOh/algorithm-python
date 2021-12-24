def max_circle_temp(queries):
    """
    해커랭크 Friend Circle Queries 솔루션

    테스트 케이스 반 정도가 시간초과 발생함
    Union find 개념 숙지 후 재구현 필요

    @Date: 2021/12/24
    @Author: Oh Donggeon
    @Link: https://www.hackerrank.com/challenges/friend-circle-queries
    """
    circle_list = list()
    answer = list()
    max_len = 0

    for query in queries:
        friend_set = {query[0], query[1]}
        temp_circle_list = list()

        for circle in circle_list:
            if not friend_set.isdisjoint(circle):
                friend_set.update(circle)
            else:
                temp_circle_list.append(circle)

        temp_circle_list.append(friend_set)
        circle_list = temp_circle_list

        max_len = max(max_len, len(friend_set))
        answer.append(max_len)

    return answer
