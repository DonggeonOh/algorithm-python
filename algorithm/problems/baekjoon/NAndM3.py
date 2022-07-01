def n_and_m(n, m):
    """
    백준 알고리즘 N과 M (3) 솔루션

    BFS로 구현하였고 백트래킹의 조건은
    1. 만들고자 하는 현재 순열에서 마지막 값이 n보다 작다면 현재 순열의 마지막 값을 pop 후 마지막 값을 증가시켜 다시 append 해준다.
    2. 현재 순열의 길이가 m보다 작다면 1을 append 해준다.

    Date: 2022/05/17
    Author: Oh Donggeon
    Link: https://www.acmicpc.net/problem/15651

    :param n: 중복 순열 중 n
    :param m: 중복 순열 중 m
    :return: 사전 순으로 n의 자연수 중 m 개의 자연수를 나열하는 2차원 배열을 반환
    """
    answer = list()
    stack = list()

    stack.append([1])

    while stack:
        cur_perm = stack.pop()

        if len(cur_perm) == m:
            answer.append(cur_perm)

        last_num_increase_perm = cur_perm.copy()
        last_num = last_num_increase_perm.pop()

        if last_num < n:
            last_num_increase_perm.append(last_num + 1)
            stack.append(last_num_increase_perm)

        new_num_append_perm = cur_perm.copy()
        new_num_append_perm.append(1)

        if len(cur_perm) < m:
            stack.append(new_num_append_perm)

    return answer


n, m = map(int, input().split())
results = n_and_m(n, m)

for result in results:
    print(*result)
