from collections import deque


def max_region_dfs_and_bfs(grid):
    """
    hacker rank DFS: Connected Cell in a Grid 솔루션

    이전 솔루션 보다 더 효율적인 DFS, BFS 솔루션

    @Date: 2021/12/14
    @Author: Oh Donggeon
    @Link: https://www.hackerrank.com/challenges/ctci-connected-cell-in-a-grid
    """
    visited = set()
    answer = 0

    for row, arr in enumerate(grid):
        for col, region in enumerate(arr):
            if grid[row][col] and (row, col) not in visited:
                # 둘 다 같은 결과
                answer = max(answer, find_regions_count_dfs(grid, visited, row, col))
                answer = max(answer, find_regions_count_bfs(grid, visited, row, col))

    return answer


def find_regions_count_dfs(grid, visited, row, col):
    """DFS 솔루션"""
    stack = [(row, col)]

    visited.add((row, col))
    count = 0

    while stack:
        row, col = stack.pop()
        count += 1

        for range_row in range(-1, 2):
            for range_col in range(-1, 2):
                target_row, target_col = row + range_row, col + range_col

                if is_index_valid(target_row, target_col, len(grid), len(grid[0])):
                    if grid[target_row][target_col] and (target_row, target_col) not in visited:
                        stack.append((target_row, target_col))
                        visited.add((target_row, target_col))

    return count


def find_regions_count_bfs(grid, visited, row, col):
    """BFS 솔루션"""
    queue = deque([(row, col)])

    visited.add((row, col))
    count = 0

    while queue:
        row, col = queue.popleft()
        count += 1

        for range_row in range(-1, 2):
            for range_col in range(-1, 2):
                target_row, target_col = row + range_row, col + range_col

                if is_index_valid(target_row, target_col, len(grid), len(grid[0])):
                    if grid[target_row][target_col] and (target_row, target_col) not in visited:
                        visited.add((target_row, target_col))
                        queue.append((target_row, target_col))

    return count


def is_index_valid(row, col, max_row, max_col):
    return 0 <= row < max_row and 0 <= col < max_col
