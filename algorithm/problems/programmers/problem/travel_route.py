from collections import deque


def travel_route(tickets):
    """
    프로그래머스 코딩테스트 고득점 Kit
    DFS BFS: 여행 경로 솔루션

    Author: Oh Donggeon
    Date: 2022/03/30
    Link: https://programmers.co.kr/learn/courses/30/lessons/43164

    :param tickets: 출발지와 도착지 티켓 배열을 감싸는 배열 [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
    :return: 출발지부터 모든 도시를 방문하는 경로를 배열로 반환, 만약 여러 개 일 경우 오름차순으로 판단
    """
    route = ['ICN']
    queue = deque()
    answer = []

    queue.appendleft((route, [False for _ in range(len(tickets))]))

    while queue:
        route, visited = queue.pop()

        if len(route) == len(tickets) + 1:
            answer.append(route)
            continue

        for index, ticket in enumerate(tickets):
            source, dest = ticket
            last_dest = route[-1]

            if source == last_dest and not visited[index]:
                next_route = route[:]
                next_visited = visited[:]

                next_route.append(dest)
                next_visited[index] = True

                queue.appendleft((next_route, next_visited))

    return min(answer)
