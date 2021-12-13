# 리스트 범위 지정
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(arr[0:2])  # 0부터 2 미만
print(arr[:6])   # 처음부터 6 미만
print(arr[7:])  # 7번째 부터 끝까지
print(arr[-7:])  # 맨 뒤에서 7번째 부터 끝까지


# Extended Slice 확장된 슬라이스 방법
# [a:b:c]
# a - 처음 index
# b - 마지막 index
# c - 띄엄띄엄 할 칸 수
# a 인덱스 이상 b 인덱스 미만까지 c만큼 띄워서 값을 가져온다.
# default 값들
# a - 처음, b - 마지막, c - 1
arr = [1, 2, 3, 4, 5]
print(arr[0:3:1])  # 0부터 3미만의 인덱스까지 1칸 씩 가져옴 - 1, 2, 3
print(arr[:4:2])  # 처음 부터 4미만까지 2칸 씩 가져옴 - 1, 3
print(arr[1::3])  # 1부터 마지막까지 3칸 씩 가져옴 - 2, 5
print(arr[::-1])  # 마지막부터 처음까지 거꾸로 1칸 씩 가져옴 - 5, 4, 3, 2, 1
print(arr[4:1:-2])  # 4부터 1미만까지 거꾸로 2칸 씩 가져옴 - 5, 3
print(arr[::])  # 처음부터 끝까지 1칸 씩 슬라이싱 - 1, 2, 3, 4, 5
# 인덱스를 음수로 접근해서도 가능하다
print(arr[-2:5:])  # 4, 5 를 가져온다.
print(arr[2:-1:]) # 3, 4 를 가져온다.


# 리스트 추가
arr = [0, 1, 2]
arr.append(3)
arr.insert(1, 4)
arr.pop()  # 맨 뒤의 값을 빼고 값 반환
arr.sort()  # 오름차순 정렬 reverse=False 기본
arr.sort(reverse=True)  # 내림차순
arr.reverse()  # 순서 뒤집기
arr.clear()  # 모든 값 지우기
arr.extend([5, 6, 7])  # 해당 인자의 리스트와 합쳐짐
print(arr)

# 리스트에 다양한 자료형 추가 가능
arr = [1, True, 'Hi']
print(arr)
