from collections import defaultdict


def freq_query(queries):
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
