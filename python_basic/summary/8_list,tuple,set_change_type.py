# 튜플, 리스트, 셋 3가지는 타입이 변경 가능하다
# 이렇게 3가지 타입을 마음대로 바꿀 수 있다
values = {1, 2, 3}
set_to_tuple = tuple(values)
set_to_list = list(values)
list_to_set = set(set_to_list)
print(values)
print(set_to_tuple)
print(set_to_list)
print(list_to_set)
