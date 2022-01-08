def union_parent(table, a, b):
    """
    두 집합간의 parent도 같이 바뀌어야 하는데 바뀌지 않아 다시 짤 필요가 있음
    """
    union_a = find_parent(table, a)
    union_b = find_parent(table, b)

    if union_a < union_b:
        table[b] = union_a
    else:
        table[a] = union_b


def find_parent(table, index):
    stack = list()

    while table[index] != index:
        stack.append(index)
        index = table[index]

    while stack:
        table_index = stack.pop()
        table[table_index] = index

    return index
