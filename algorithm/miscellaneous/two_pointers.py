def two_pointers(seq, target):
    """
    리스트에 순차적으로 접근해야 할 때 두 개의 점 위치를 기록하면서 처리하는 알고리즘이다.
    투 포인터 알고리즘은 어떤 시퀀스에서 부분 연속 수열의 값을 더해 특정 값이 몇 번 나오는지를 확인 할 때
    완전 탐색의 경우 O(N^2)의 시간이 소요되지만 투 포인터를 이용하면 O(N) 만큼의 시간복잡도가 소요된다.
    :param seq: iterable한 데이터
    :param target: 부분 연속 수열을 모두 더한 값의 특정 값
    :return: target이 몇 번 나왔는지 횟수를 반환
    """
    start, end = 0, 0
    sum = 0
    count = 0
    # 끝 인덱스가 seq 길이이고 sum의 값이 구하려는 값보다 작으면 더이상 구할 수 없으므로 빠져나온다.
    while end != len(seq) or sum >= target:
        if sum >= target:
            if sum == target:
                count += 1
            sum -= seq[start]
            start += 1
        else:
            sum += seq[end]
            end += 1

    return count


def two_pointers_e_co_te(seq, target):
    """이코테 2021 강의 자료에 나오는 투 포인터 구현 코드"""
    count = 0
    sum = 0
    end = 0

    for start in range(len(seq)):
        while sum < target and end < len(seq):  # end 를 타겟 넘버 미만으로 가능한 만큼 끝까지 돌린다.
            sum += seq[end]
            end += 1

        if sum == target:
            count += 1

        sum -= seq[start]

    return count
