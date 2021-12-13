# 학교에서 파이썬 코딩 대회를 주최합니다.
# 참석률을 높이기 위해 댓글 이벤트를 진행하기로 하였습니다.
# 댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다.
# 추첨 프로그램을 작성하시오.
#
# 조건1 : 편의상 댓글은 20명이 작성하였고 아이디는 1~20 이라고 가정
# 조건2 : 댓글 내용과 상관 없이 무작위로 추첨하되 중복 불가
# 조건3 : random 모듈의 shuffle 과 sample 을 활용
#
# 예제)
# --당첨자 발표--
# 치킨 당첨자 : 1
# 커피 당첨자 : [2, 3, 4]
# --축하합니다--

from random import shuffle, sample

participants = range(1, 21)  # 1 부터 20 까지 range 클래스 생성
participants = list(participants)  # range 클래스를 list 클래스에 넣어 초기화 하면 1~20의 숫자 완성

shuffle(participants)

chicken_dinner = sample(participants, 1)
coffee_winner = sample(participants, 3)

print('--당첨자 발표--')
print('치킨 당첨자 : ', chicken_dinner[0])
print('커피 당첨자 : ', coffee_winner)
print('--축하 합니다--')