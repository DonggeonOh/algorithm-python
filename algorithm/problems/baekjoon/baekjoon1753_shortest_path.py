import sys
from heapq import *


input = sys.stdin.readline
maxsize = sys.maxsize


def shortest_path(graph, start):
    """
    백준 1753번 최단경로 솔루션

    @Date: 2021/01/05
    @Author: Oh Donggeon
    @Link: https://www.acmicpc.net/problem/1753

    :param graph: 2차원 배열로 된 그래프 (배열 원소에는 해당 인덱스에서 다음 정점 및 거리가 들어가 있음)
    :param start: 시작 정점
    :return: 시작 정점에서 모든 정점의 최소 거리
    """
    shortest_distance = [maxsize for _ in range(len(graph))]
    heap = []

    heappush(heap, (0, start))
    shortest_distance[start] = 0

    while heap:
        distance, min_vertex = heappop(heap)

        if distance > shortest_distance[min_vertex]:
            continue

        for target_vertex, edge in graph[min_vertex]:
            target_distance = shortest_distance[min_vertex] + edge

            if target_distance < shortest_distance[target_vertex]:
                shortest_distance[target_vertex] = target_distance
                heappush(heap, (target_distance, target_vertex))

    return shortest_distance


""" 백준 input code
input_graph = list(map(int, input().split()))
input_start_vertex = int(input())

graph = [[] for _ in range(input_graph[0] + 1)]

for _ in range(input_graph[1]):
    vertex, target_vertex, edge = list(map(int, input().split()))
    graph[vertex].append((target_vertex, edge))

result = shortest_path(graph, input_start_vertex)

for index in range(1, len(result)):
    print("INF" if result[index] == maxsize else result[index])
"""
# Test code
test_file = open('baekjoon1753_shortest_path_test_data.txt', 'r', encoding='utf8')
init_graph = list(map(int, test_file.readline().split()))
input_start_vertex = int(test_file.readline())

graph = [[] for _ in range(init_graph[0])]

for _ in range(init_graph[1]):
    temp = list(map(int, test_file.readline().split()))
    graph[temp[0] - 1].append((temp[1] - 1, temp[2]))

results = shortest_path(graph, input_start_vertex - 1)

for result in results:
    print("INF" if result == maxsize else result)

test_file.close()
