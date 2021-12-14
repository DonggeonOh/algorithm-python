# Dictionary 선언 및 메서드
dictionary = {1: 'Hi', 2: 'Hello'}
print(dictionary[2])  # 만약 인덱스로 없는 key에 접근하게 된다면 런타임 오류 발생
print(dictionary.get(2))  # None을 출력하고 런타임 오류가 발생하지 않는다
# 2에 해당하는 value가 없으면 Bonjour를 추가하고 있다면 해당 value를 가져온다.
print(dictionary.setdefault(2, 'Bonjour'))
print(3 in dictionary)  # False, key 값이 3인 value가 있는지 묻는 것
print(dictionary.keys())  # 모든 key 값
print(dictionary.values())  # 모든 value 값
print(dictionary.items())  # 모든 Item 값
del dictionary[1]  # 해당 값을 지운다 인덱스가 없다면 런타임 오류 발생
dictionary.clear()  # 모든 값 지우기
