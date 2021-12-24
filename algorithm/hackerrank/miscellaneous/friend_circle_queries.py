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


from collections import defaultdict


def max_circle_union_find_array(queries):
    """
    해커랭크 Friend Circle Queries 솔루션 - Union find 배열 구현

    union 시 갯수도 같이 세도록 구현했지만 시간초과 발생
    추후 Tree로 재구현 필요 (https://en.wikipedia.org/wiki/Disjoint-set_data_structure)

    @Date: 2021/12/24
    @Author: Oh Donggeon
    @Link: https://www.hackerrank.com/challenges/friend-circle-queries
    """
    circledict = defaultdict(int)
    answer = list()

    for query in queries:
        countdict = defaultdict(int)
        friendA = query[0]
        friendB = query[1]

        answer.append(union(circledict, countdict, friendA, friendB))

    return answer


def union(circledict, countdict, friendA, friendB):
    leftval = find(circledict, friendA)
    rightval = find(circledict, friendB)
    maxval = max(countdict[leftval], countdict[rightval])

    for key in circledict:
        if circledict[key] == rightval:
            circledict[key] = leftval
            countdict[leftval] = countdict[leftval] + 1 if countdict[leftval] else 1
            maxval = max(maxval, countdict[leftval])
            continue

        if countdict[circledict[key]]:
            countdict[circledict[key]] += 1
        else:
            countdict[circledict[key]] = 1

        maxval = max(maxval, countdict[circledict[key]])

    return maxval


def find(circledict, key):
    if not circledict[key]:
        circledict[key] = key

    return circledict[key]
