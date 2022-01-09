from algorithm.union_finds.minimum_spanning_tree import minimum_spanning_tree


test_file = open("minimum_spanning_tree_test_data.txt", "r", encoding="utf8")
vertex, edge = map(int, test_file.readline().split())
graph = [[0 for _ in range(vertex + 1)] for _ in range(vertex + 1)]

for _ in range(edge):
    v1, v2, e = map(int, test_file.readline().split())
    graph[v1][v2] = e

spanning_tree = minimum_spanning_tree(graph)

for row in range(len(graph)):
    print(spanning_tree[row])

test_file.close()
