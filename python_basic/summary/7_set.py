# Set 초기화 및 메서드
# Set은 알다시피 중복이 불가능한 타입이다.
set1 = {1, 2, 3, 3, 3}  # or set = set([1, 2, 3, 3, 3])
print(set1)  # {1, 2, 3}


# 교집합 출력
set2 = {2, 3, 4, 5, 6}
print(set1 & set2)  # {2, 3}
print(set1.intersection(set2))


# 합집합 출력
print(set1 | set2)  # {1, 2, 3, 4, 5, 6}
print(set1.union(set2))


# 차집합 출력
print(set1 - set2)  # {1}
print(set1.difference(set2))


# 집합 값 추가
set1.add(4)
print(set1)  # {1, 2, 3, 4}
set1.update([5, 6, 7])
print(set1)  # {1, 2, 3, 4, 5, 6, 7}


# 집합 값 제거
set1.remove(1)  # 해당 값이 없는경우 런타임 에러 발생
print(set1)  # {2, 3, 4, 5, 6, 7}
# discard는 runtime 오류를 발생 시키지 않음
set1.discard(1)  # 해당 값이 있는경우 삭제
print(set1)  # {2, 3, 4, 5, 6, 7}
