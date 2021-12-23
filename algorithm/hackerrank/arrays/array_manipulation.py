def array_manipulation(queries):
    """
    해커랭크 Array manipulation 솔루션

    문제의 관건은 모든 값을 더하고 빼는 것이 아니라
    누적합을 이용하여 해당 인덱스의 값을 상대적으로 구하는것이 관건이다.
    누적합 배열을 만드는 법은 인터넷에 많이 나와있으니 참고하자.
    """
    sum_dict = dict()
    answer = 0
    temp = 0

    for query in queries:
        start_index, end_index, value = query

        add_dict_prefix_sum(sum_dict, start_index - 1, value)
        add_dict_prefix_sum(sum_dict, end_index, -value)

    for key in sorted(sum_dict.keys()):
        temp += sum_dict[key]
        answer = max(answer, temp)

    return answer


def add_dict_prefix_sum(sum_dict, index, value):
    if sum_dict.get(index):
        sum_dict[index] += value
    else:
        sum_dict.setdefault(index, value)
