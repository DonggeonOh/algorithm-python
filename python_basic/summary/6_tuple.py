# Tuple 초기화 및 메서드
tuple1 = ("돈까스", "치즈 돈까스")
tuple2 = ('a', 'b', ('ab', 'cd'))  # 다양한 자료형을 넣을 수 있다.
name, age, gender = ('Oh Donggeon', 26, 'Male')  # 각각 다른 변수로 unpacking


# 튜플도 list와 마찬가지로 [:2] 와 같이 범위를 통해 값을 가져올 수 있다.
t = (1, 2, 'a', 'b')
print(t[1:])  # (2, 'a', 'b')


# 튜플에서 더하기 및 곱하기 연산이 가능하다.
t1 = (1, 2, 'a', 'b')
t2 = (3, 4)
print(t1 + t2)  # (1, 2, 'a', 'b', 3, 4)
t3 = (3, 4)
print(t3 * 3)  # (3, 4, 3, 4, 3, 4)
