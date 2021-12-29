def binary_search_right_most(seq, target):
    """
    중복된 값이 있는 경우의 가장 오른쪽 인덱스를 반환하는 이진탐색

    :param seq: 정렬 되어있는 Sequence
    :param target: input 에서 찾으려고 하는 값
    :return target이 위치한 index 반환
    """
    if not seq:
        return None

    low = 0
    high = len(seq) - 1

    while low < high:
        mid = int((low + high) / 2)

        if seq[mid] <= target:
            low = mid + 1
        else:
            high = mid

    high -= 1

    return high if seq[high] == target else None
