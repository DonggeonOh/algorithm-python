from collections import deque


def max_region(grid):
    """
    hacker rank DFS: Connected Cell in a Grid 솔루션

    @Date: 2021/12/13
    @Author: Oh Donggeon
    @Link: https://www.hackerrank.com/challenges/ctci-connected-cell-in-a-grid
    """
    visited = [[False] * len(arr) for arr in grid]
    answer = 0

    for row, arr in enumerate(grid):
        for col, element in enumerate(arr):
            if element == 0 or visited[row][col]:
                continue
            expected = find_region_count(grid, visited, row, col)
            answer = expected if answer < expected else answer

    return answer


def find_region_count(grid, visited, row, col):
    """
    해당 row, col 에서 주변 8칸이 1 인 경우를 찾아서 해당하는 모든 인덱스를 stack 에 넣고
    찾은 인덱스 또한 그 주변의 8칸의 값이 1인 경우를 따져 주변의 지역의 갯수를 반환 한다.

    :param grid: 0과 1로 되어있는 2차원 배열
    :param visited: grid 인덱스의 접근 여부를 확인하는 Bool 타입의 2차원 배열
    :param row: grid의 row
    :param col: grid의 col
    :return: 해당 위치의 region의 모든 갯수를 반환한다.
    """
    stack = deque()
    count = 0

    stack.append((row, col))
    visited[row][col] = True

    while stack:
        row, col = stack.pop()
        count += 1

        if row != 0:  # top
            append_stack_is_not_visited(grid, stack, visited, row - 1, col)
            if col != 0:  # top left
                append_stack_is_not_visited(grid, stack, visited, row - 1, col - 1)
            if col != len(grid[row]) - 1:  # top right
                append_stack_is_not_visited(grid, stack, visited, row - 1, col + 1)
        if row != len(grid) - 1:  # bottom
            append_stack_is_not_visited(grid, stack, visited, row + 1, col)
            if col != 0:  # bottom left
                append_stack_is_not_visited(grid, stack, visited, row + 1, col - 1)
            if col != len(grid) - 1:  # bottom right
                append_stack_is_not_visited(grid, stack, visited, row + 1, col + 1)

        if col != 0:  # left
            append_stack_is_not_visited(grid, stack, visited, row, col - 1)
        if col != len(grid[row]) - 1:  # right
            append_stack_is_not_visited(grid, stack, visited, row, col + 1)

    return count


def append_stack_is_not_visited(grid, stack, visited, row, col):
    if not 0 <= row < len(grid):
        pass
    elif not 0 <= col < len(grid[row]):
        pass
    elif grid[row][col] == 1 and not visited[row][col]:
        stack.append((row, col))
        visited[row][col] = True
