def counting_sort(values, max_value):
    count_list = [0 for _ in range(0, max_value + 1)]  # [0] * (max_value + 1)
    sorted_values = [0 for _ in range(len(values))]  # [0] * len(values)

    for value in values:
        count_list[value] += 1

    for index in range(1, max_value + 1):
        count_list[index] += count_list[index - 1]

    for index in range(len(values) - 1, -1, -1):
        count_list[values[index]] -= 1
        sorted_values[count_list[values[index]]] = values[index]

    return sorted_values
