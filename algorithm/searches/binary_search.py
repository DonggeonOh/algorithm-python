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
