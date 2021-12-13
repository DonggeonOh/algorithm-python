# 표준 체중을 구하는 프로그램을 작성하시오
#
# 표준 체중 : 각 개인의 키에 적당한 체중
#
# 남자: 키(m) * 키(m) * 22
# 여자: 키(m) * 키(m) * 21
#
# 조건1: 표준 체중은 별도의 함수 내에서 계산
# * 함수 명: std_weight
# * 전달 값: 키(height), 성별(gender)
# 조건2: 표준 체중은 소수점 둘째자리까지 표시
#
# 출력 예제
# 키 175cm 남자의 표준 체중은 67.38kg 입니다.
def std_weight(height, gender):
    if gender == 'm' or gender == 'male':
        return height * height * 22
    else:
        return height * height * 21


weight = std_weight(1.71, 'm')
print('%.2f' % weight)
print(round(weight, 2))
