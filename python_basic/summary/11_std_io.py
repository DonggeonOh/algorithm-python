# 표준 입출력 관련 매개변수
import sys
print('python', 'swift', sep=', ')  # separator - python, swift
print('python', 'swift', sep=' vs ')  # python vs swift
print('python', 'swift', sep=' vs ', end=' the end\n') # end - 기본값은 \n 개행이다. python vs swift the end
print('python', 'swift', file=sys.stdout)  # 표준 출력이다. 로그 분석을 할 때 값이 잘 나오는지 확인하기 위해 사용
print('python', 'swift', file=sys.stderr)  # 표준 에러이다. 어떤 문제가 있어 로그로 표준 에러로 출력하고자 할 때 사용


# 왼쪽 or 오른쪽 정렬
# str.ljust(숫자) - 숫자만큼의 공간을 확보 후 왼쪽정렬
# str.rjust(숫자) - 숫자만큼의 공간을 확보 후 오른쪽정렬
scores = {'math':90, 'physics':80, 'science':70}
for subject, score in scores.items():
    print(subject.ljust(8), str(score).rjust(3), sep=':')

# 숫자에서 001, 002... 와 같이 표기하기
# str.zfill(숫자) - 숫자만큼의 자릿수만큼 0을 채움
for num in range(10):
    print(str(num).zfill(3), end=' ')  # 000, 001, 002...
print()


# 콘솔에서 입력 받기
# input_console = input()  # input()은 항상 str로 반환한다
# print('input : {}'.format(input_console))


# 빈공간을 확보하는 다른 방법
print('{0: >5}'.format(300))  # 앞은 빈공간으로 하고, 5 만큼 공간확보 및 오른쪽 정렬
print('{0:0>5}'.format(300))  # 앞은 0으로 하고, 5 만큼의 공간확보 및 오른쪽 정렬 00300 이 출력된다.
print('{0: >+5}'.format(300))  # +가 붙으면 양수 및 음수가 출력된다. +500
print('{0: >+5}'.format(-300))  # -500
print('{0: <+5}'.format(-300))  # 왼쪽정렬


# 숫자에서 3자리마다 , 찍기
print('{0:,}'.format(100000000))  # 100,000,000 출력
print('{0:+,}'.format(100000000))  # +100,000,000 출력


# 소수점 출력 및 특정 자릿수 까지만 표시
print('{0:f}'.format(3.1415926))  # 6자리 까지 소수출력
print('{0:.2f}'.format(3.1415926))  # 3.14
