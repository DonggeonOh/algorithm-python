def prime_number(num):
    """
    일반적인 소수를 구하기 위한 알고리즘
    해당 알고리즘의 시간 복잡도는 O(n) 일 것이다.
    소수를 찾기 위해선 좀 더 효율적인 알고리즘이 존재한다.

    :param num: 소수인지 판별하는 2 이상의 정수
    :return: 소수이면 True, 아니라면 False 반환
    """
    if num <= 0:
        return None
    elif num == 1:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True
