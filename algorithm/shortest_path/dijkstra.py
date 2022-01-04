from sys import maxsize
from heapq import *


def dijkstra(graph, start, end):
    shortest_distance = [maxsize for _ in range(graph.len)]
    visited = set()

    shortest_distance[start] = 0

    for _ in range(graph.len):
        min_vertex = min_distance_vertex(shortest_distance, visited)
        visited.add(min_vertex)

        for vertex, edge in enumerate(graph.edges(min_vertex)):
            if edge and shortest_distance[min_vertex] + edge < shortest_distance[vertex]:
                shortest_distance[vertex] = shortest_distance[min_vertex] + edge

    return None if shortest_distance[end] == maxsize else shortest_distance[end]


def min_distance_vertex(iter, visited):
    min_value = maxsize
    min_index = maxsize

    for index, value in enumerate(iter):
        if index not in visited and value < min_value:
            min_index = index

    return None if min_value == maxsize else min_index


def dijkstra_min_heap(graph, start, end):
    shortest_distance = init_shortest_distance_tuple_list(graph.len)
    visited = set()

    heapify(shortest_distance)

    for _ in range(graph.len):
        min_vertex = heappop(shortest_distance)
        visited.add(min_vertex[1])

        for vertex, edge in enumerate(graph.edges(min_vertex)):
            if edge and shortest_distance[min_vertex[0]][0] + edge < shortest_distance[vertex][0]:
                shortest_distance[vertex][0] = (shortest_distance[min_vertex[0]][0] + edge, vertex)

    return None if shortest_distance[end] == maxsize else shortest_distance[end]


def init_shortest_distance_tuple_list(len):
    result = [(maxsize, index) for index in range(len)]

    result[0] = (0, 0)

    return result
