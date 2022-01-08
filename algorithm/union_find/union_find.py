def union_parent(table, a, b):
    union_a = find_parent(table, a)
    union_b = find_parent(table, b)

    if union_a < union_b:
        table[b] = union_a
    else:
        table[a] = union_b


def find_parent(table, index):
    while table[index] != index:
        index = table[index]

    return table[index]
