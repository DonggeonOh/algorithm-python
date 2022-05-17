def binary_gap(n):
    """
    코딜리티 Binary gap 문제 솔루션

    :param n: 자연수
    :return: n을 이진수로 표현 하였을 때 1과 0 사이의 최대 간격 (100101의 경우 2, 1000의 경우 0을 반환)
    """
    bin_str = str(format(n, 'b'))
    answer = 0
    max_gap = 0

    for index in range(1, len(bin_str)):
        if bin_str[index] == '1':
            if answer < max_gap:
                answer = max_gap
            max_gap = 0
        else:
            max_gap += 1

    return answer
