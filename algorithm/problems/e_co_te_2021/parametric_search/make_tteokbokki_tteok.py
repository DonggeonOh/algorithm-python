def make_tteokbokki_tteok(tteoks, length):
    """
    파라메트릭 서치란 최적화 문제("예" 혹은 "아니요")로 바꾸어 해결하는 기법을 말한다
    일반적으로 코딩 테스트에서 파라메트릭 서치 문제는 이진 탐색을 이용하여 문제 해결이 가능하다
    ex) 특정한 조건을 만족하는 가장 알맞은 값을 빠르게 찾는 최적화 문제
    :param tteoks: 떡의 길이가 담긴 리스트
    :param length: 손님이 가져갈 떡의 최소 길이
    """
    low_length = 0
    high_length = max(tteoks)
    max_length = high_length

    while low_length <= high_length:
        mid_length = int((low_length + high_length) / 2)
        target_length = 0

        for tteok in tteoks:
            if tteok - mid_length > 0:
                target_length += tteok - mid_length

        if target_length > length:
            max_length = mid_length
            low_length = mid_length + 1

        elif target_length < length:
            high_length = mid_length - 1

        else:
            return mid_length

    return max_length

answer = make_tteokbokki_tteok([19, 15, 10, 17], 6)
print(answer)