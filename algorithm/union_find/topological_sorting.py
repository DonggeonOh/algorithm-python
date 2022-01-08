from collections import deque


def topological_sorting(graph):
    """
        싸이클이 없는 방향 그래프(Directed Acyclic Graph)의 모든 노드를
        방향성에 거스르지 않도록 한마디로 순서를 나열하여 순서대로 나열한 것이다.
        위상정렬의 경우 여러가지의 결과가 나올 수 있다.
        구현의 경우 DFS, Queue 를 이용하여 구현할 수 있고 Queue를 사용하여 구현 하였다.

        :param graph: 인접행렬로 구현된 그래프
        :return: 정점의 정렬 순서
    """
    incoming_edges = get_incoming_edges(graph)
    queue = deque()
    result = list()

    for index in range(1, len(incoming_edges)):
        if not incoming_edges[index]:
            queue.append(index)

    while queue:
        vertex = queue.popleft()
        result.append(vertex)

        for index in range(1, len(graph[vertex])):
            if graph[vertex][index]:
                incoming_edges[index] -= 1

                if not incoming_edges[index]:  # 다음 정점의 진입 차수가 0 인 경우 Queue 에 넣는다.
                    queue.append(index)

    return result


def get_incoming_edges(graph):
    incoming_edges = [0 for _ in range(len(graph))]

    for row in range(1, len(graph)):
        for col in range(1, len(graph[row])):
            if graph[row][col]:
                incoming_edges[col] += 1

    return incoming_edges
