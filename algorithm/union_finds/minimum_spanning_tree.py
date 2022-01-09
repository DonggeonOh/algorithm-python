from algorithm.union_finds.union_find import *


def minimum_spanning_tree(graph):
    """
    크루스칼 알고리즘을 사용하면 쉽게 최소 신장트리를 구할 수 있다.
    크루스칼 알고리즘은 욕심쟁이 알고리즘을 사용하며 간선을 오름차순으로 정렬한 후에
    간선을 잇는 두 정점이 사이클이 발생하는지 아닌지에 따라서 발생하면 해당 간선을 포합하지 않는 방법으로
    최소 신장 트리를 만들 수 있다. 사이클 판단 여부는 Union find 를 활용하면 쉽게 판단 가능하다.
    간선의 갯수가 E 개 일 때, O(ElogE) 의 시간복잡도를 가진다.
    크루스칼 알고리즘에서 가장 많은 시간이 걸리는 부분은 간선을 정렬할 때 가장 많은 시간을 소요한다.
    따라서 어떤 정렬 알고리즘을 사용하는지에 따라 시간복잡도가 결정되게 되는데 표준라이브러리를 이용하여 정렬을 수행하면
    파이썬의 경우 O(nlogn)을 보장해주기 때문에 E 만큼의 간선의 갯수를 정렬해줘야 하므로 O(ElogE) 만큼의 시간이 소요된다.
    """
    result = [[0 for _ in range(len(graph))] for _ in range(len(graph))]
    union_table = [parent for parent in range(len(graph))]
    sorted_edges = sort_edges(graph)

    for edge in sorted_edges:
        weight, vertex, next_vertex = edge

        if find_parent(union_table, vertex) != find_parent(union_table, next_vertex):
            union_parent(union_table, vertex, next_vertex)

            result[vertex][next_vertex] = weight

    return result


def sort_edges(graph):
    result = list()

    for row in range(len(graph)):
        for col in range(len(graph[row])):
            if graph[row][col]:
                result.append((graph[row][col], row, col))

    result.sort()

    return result
