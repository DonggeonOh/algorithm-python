def sherlock_and_anagrams(s):
    """
    해커랭크 Sherlock and Anagrams 솔루션

    솔루션 설명
    1. 문자열에서 조합 가능한 모든 부분 문자열을 만들고 정렬하여 딕셔너리에 넣는다.
    1-1. 이중포문을 돌면서 부분 문자열을 만든다.
    1-2. 딕셔너리에 값이 있다면 해당 부분 문자열의 value 값을 1 증가시킨다.
    1-3. 딕셔너리에 값이 없다면 해당 부분 문자열을 딕셔너리에 추가하고 value는 1로 초기화시킨다.
    2. 모든 부분 문자열에 대하여 딕셔너리에 값을 다 넣었다면 모든 value에 대한 조합을 모두 더해 반환한다.
    2-1. for문을 통해 dict.values(self)를 하나 씩 가져온다.
    2-2. 조합 공식은 n! / (n - r)!r! 이다. n - 모든 갯수, r - 뽑아야 할 갯수
         nC2 의 경우 n(n-1) / 2 이므로 모든 value에 대해 식을 대입해 주면 된다.
    """
    target_dict = dict()
    answer = 0

    for x in range(len(s)):
        for y in range(x, len(s)):
            target = "".join(sorted(s[x:y + 1]))

            if target in target_dict:
                target_dict[target] += 1
            else:
                target_dict.setdefault(target, 1)

    for result in target_dict.values():
        answer += result * (result - 1) / 2

    return int(answer)
