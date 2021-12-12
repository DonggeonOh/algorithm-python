# 소수점 관련 라이브러리
from math import *  # math 라이브러리 안에 있는 모든 함수 불러오기

print(floor(3.14))  # 내림
print(ceil(3.14))  # 올림
print(sqrt(16))  # 제곱근 - 16의 제곱근 4
print(round(3.1415926, 3))  # 소수점 셋째자리 까지

# 랜덤 관련 라이브러리
from random import *

print(random())  # 0.0 부터 1.0 사이의 소수점 값 반환
print(random() * 10)  # 0.0 부터 10.0 사이의 소수점 값 반환
print(randrange(0, 5))  # A 이상 B 미만의 랜덤한 정수 값 반환
print(randint(6, 10))  # A 이상 B 이하의 랜덤한 정수 값 반환
