from collections import deque


def network(n, network):
    """
    프로그래머스 코딩테스트 고득점 Kit
    DFS BFS: 네트워크 솔루션

    Author: Oh Donggeon
    Date: 2022/03/29
    Link: https://programmers.co.kr/learn/courses/30/lessons/43162
    :param n: 노드의 갯수
    :param network: 네트워크에 연결된 컴퓨터가 표현된 2차원 배열
    :return: 연결된 네트워크의 갯수
    """
    visited = [False for _ in range(n)]
    answer = 0

    for index, visit_node in enumerate(visited):
        if not visit_node:
            queue = deque([index])

            while queue:
                node_index = queue.pop()
                visited[node_index] = True

                for next_node, connected in enumerate(network[node_index]):
                    if connected == 1 and not visited[next_node]:
                        queue.appendleft(next_node)

            answer += 1

    return answer
