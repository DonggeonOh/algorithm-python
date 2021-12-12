# Cocoa 서비스를 이용하는 택시 기사이다.
# 50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수 를 구하는 프로그램을 작성하시오.
#
# 조건1 : 승객별 운행 소요 시간은 5분 ~ 50분 사이의 난수로 정해진다.
# 조건2 : 당신은 소요 시간 5분 ~ 15분 사이의 승객만 매칭해야 한다.
#
# 출력문 예제
# [O] 1번째 손님 (소요시간 : 15분)
# [ ] 2번째 손님 (소요시간 : 50분)
# [O] 3번째 손님 (소요시간 : 5분)
# ...
# [ ] 50번째 손님 (소요시간 : 16분)
#
# 총 탑승 승객 : 2 분
from random import *
passenger = 0
for index in range(50):
    required_time = randint(5, 50)
    if 5 <= required_time <= 15:
        print('[O] {0}번째 손님 (소요시간 : {1}분)'.format(index + 1, required_time))
        passenger += 1
    else:
        print('[ ] {0}번째 손님 (소요시간 : {1}분)'.format(index + 1, required_time))
print("총 탑승 승객 : {0} 분".format(passenger))