def floyd_warshall(graph):
    """
    플로이드 워셜 알고리즘
    Dab = min(Dab, Dak + Dkb)
    위의 식을 점화식으로 하여 다이나믹 프로그래밍 방법으로 알고리즘을 구현할 수 있다.
    간단한 알고리즘이지만 시간 복잡도는 O(n^3) 으로 정점이 많을 경우 시간이 매우 오래걸린다.
    그래프는 인접행렬로 표현하였다.
    """
    for k in range(1, len(graph)):
        for a in range(1, len(graph)):
            for b in range(1, len(graph)):
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

    return graph
