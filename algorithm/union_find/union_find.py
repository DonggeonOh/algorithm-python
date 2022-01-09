def union_parent(table, a, b):
    a = find_parent(table, a)
    b = find_parent(table, b)

    if a < b:
        table[b] = a
    else:
        table[a] = b


def find_parent(table, index):
    stack = list()

    while table[index] != index:
        stack.append(index)
        index = table[index]

    while stack:
        table_index = stack.pop()
        table[table_index] = index

    return index
