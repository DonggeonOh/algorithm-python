from collections import defaultdict


def freq_query(queries):
    """
    해커랭크 Frequency queries 솔루션

    문제의 핵심 관건은 query[0] == 2 인 경우에
    query[1] 과 같은 빈도 수를 가진 value를 찾는 것이였는데,
    value를 key로 가지고 빈도수를 value로 가지는 dict로 찾기엔 O(n)이 걸리므로
    또 다른 frequency를 key로 가지고 frequency의 빈도를 value로 가지는 dict를 하나 더 생성하여
    빈도수를 찾는데 O(1) 이 걸리도록 하는게 핵심
    """
    value_dict = defaultdict(int)
    frequency_dict = defaultdict(int)

    answer = list()

    for query in queries:
        if query[0] == 1:
            adjust_value_and_frequency_dict(value_dict, frequency_dict,
                                            query[1], value_dict[query[1]], 1)

        elif query[0] == 2:
            if value_dict[query[1]]:
                adjust_value_and_frequency_dict(value_dict, frequency_dict,
                                                query[1], value_dict[query[1]], -1)

        elif query[0] == 3:
            answer.append(1 if frequency_dict[query[1]] else 0)

    return answer


def adjust_value_and_frequency_dict(value_dict, frequency_dict, key, value, diff):
    value_dict[key] += diff

    frequency_dict[value] -= 1
    frequency_dict[value + diff] += 1
