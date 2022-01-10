from math import sqrt


def prime_number(num):
    """
    정수 N의 약수는 가운데 약수를 기준으로 대칭을 이룬다는 것을 알 수 있다.
    16의 경우 1, 2, 4, 8, 16 이므로, 2 X 8, 8 X 2 과 같이 4를 기준으로 대칭을 이루므로
    모든 약수를 찾을 때 해당 자연수의 제곱근 까지만 확인하면 찾을 수 있다.
    시간복잡도는 2부터 N 의 제곱근 까지 모든 자연수에 대하여 연산을 수행해야 하기 때문에 O(N^1/2) 루트 N 이다.

    :param num: 소수인지 판별하는 2 이상의 정수
    :return: 소수이면 True, 아니라면 False 반환
    """
    if num <= 0:
        return None
    elif num == 1:
        return False

    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False

    return True
