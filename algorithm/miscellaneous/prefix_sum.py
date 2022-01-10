def prefix_sum(seq, start, end):
    """
    접두사 합(Prefix sum)은 배열의 맨 앞부터 각 위치 까지의 합을 구해놓은 것을 말한다.
    어떤 시퀀스 A에 대해 i 번째 부터 j 까지의 구간 합을 계산한다고 하면
    A[j] - A[i - 1] 로 나타낼 수 있다.
    계산의 편의를 위해 첫 번째 인덱스는 0으로 초기화한다.

    :param seq: iterable 한 데이터
    :param start: 시작 인덱스
    :param end: 마지막 인덱스
    :return: 시작 인덱스 부터 마지막 인덱스 까지의 구간 합을 반환
    """
    prefix_sum_list = [0]

    for num in seq:
        prefix_sum_list.append(prefix_sum_list[-1] + num)

    return prefix_sum_list[end + 1] - prefix_sum_list[start]
