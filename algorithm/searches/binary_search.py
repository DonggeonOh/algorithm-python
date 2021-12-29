from math import ceil


def binary_search(seq, target):
    """
    이진 탐색은 정렬되어 있는 값여야 수행 가능하다.

    :param seq: 정렬 되어있는 Sequence
    :param target: input 에서 찾으려고 하는 값
    :return target이 위치한 index 반환
    """
    low = 0
    high = len(seq) - 1

    while low <= high:
        mid = int((low + high) / 2)

        if target < seq[mid]:
            high = mid - 1
        elif target > seq[mid]:
            low = mid + 1
        else:
            return mid

    return -1


def binary_search_optimize(seq, target):
    """
    위 이진탐색에서 비교문을 줄여 최적화한 이진탐색 알고리즘이다.

    :param seq: 정렬 되어있는 Sequence
    :param target: input 에서 찾으려고 하는 값
    :return target이 위치한 index 반환
    """
    low = 0
    high = len(seq) - 1

    while low < high:
        mid = ceil((low + high) / 2)

        if target < seq[mid]:
            high = mid - 1
        else:
            low = mid

    if seq[low] == target:
        return low
    else:
        return -1
