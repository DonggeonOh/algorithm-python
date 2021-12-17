def count_triplets(arr, r):
    """
    해커랭크 Count triplets 솔루션
    문제 난이도가 높아 https://www.snoopybox.co.kr/1794 위 솔루션 참고하여 해결
    """
    left, right = dict(), dict()
    answer = 0

    for element in arr:
        if right.get(element):
            right[element] += 1
        else:
            right.setdefault(element, 1)

    for element in arr:
        right[element] -= 1

        if element % r == 0:
            if left.get(element // r) and right.get(element * r):
                answer += left[element // r] * right[element * r]

        if left.get(element):
            left[element] += 1
        else:
            left.setdefault(element, 1)

    return answer
