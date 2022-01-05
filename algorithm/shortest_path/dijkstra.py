from sys import maxsize
from heapq import *


def dijkstra(graph, start, end):
    shortest_distance = [maxsize for _ in range(graph.len)]
    visited = set()

    shortest_distance[start] = 0

    for _ in range(graph.len):
        min_vertex = min_distance_vertex(shortest_distance, visited)
        visited.add(min_vertex)

        if min_vertex is not None:
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

    return None if shortest_distance[end] == maxsize else shortest_distance[end]
