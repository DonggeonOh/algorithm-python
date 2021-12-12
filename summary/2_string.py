# 문자열 초기화
str1 = '한 줄의 문자열 표현 가능 1'
str2 = "한 줄의 문자열 표현 가능 2"
str3 = """
여러 줄 표현가능
"""
print(str1)
print(str2)
print(str3)


# 문자열 처리 함수
# standard
str4 = 'test'
print(len(str4))  # 문자열의 길이 반환
# str 메소드
print(str4.lower())  # 모든 문자열을 소문자로 만듦
print(str4.upper())  # 모든 문자열을 대문자로 만듦
print(str4[0].islower())  # 첫번째 문자열이 소문자인지 아닌지 bool 반환
print(str4[0].isupper())  # 첫번째 문자열이 대문자인지 아닌지 bool 반환
# 기본 값은 -1로 위의 replace(old str, new str)과 같이 사용하면 전체 다 new로 바뀜
print(str4.replace(str4, "replaced str4"))  # 어떤 문자열과 같은 부분을 새로운 값으로 교체
print(str4.replace(str4, "replaced str4 2", 3))  # new str로 교체하지만 int 수 만큼 앞에서 바꾼 후 종료
# 문자가 아닌 문자열의 경우 해당 문자열의 index를 찾고 첫번째 인덱스를 반환한다.
# ex) str.index('st') - 2 반환
print(str4.index('e'))  # 해당 문자가 있는 index 반환
print(str4.index('e', 0, 5))  # start부터 end 인덱스 미만의 해당 문자의 index 반환
print(str4.index('t', 2))  # 2 부터 끝까지
# .index() 와 같이 똑같이 index를 반환하지만, 만약 찾는 값이 없는경우 -1 반환
print(str4.find('e'))
print(str4.find('e', 0, 5))
print(str4.find('0', 2))
# 마찬가지로 위 index, find 와 같이 범위 지정 가능하다!!
print(str4.count(str4))  # 해당 문자열이 몇개 들어가있는지 count 함


# 문자열 형식지정자 (Format specifier)
print('test %d' % 10)  # test 10
print('test %s' % 'test')  # test test
print('test %c' % 't')  # test t
print('test %s %s' % ('test2', 'test3'))  # test test2 test3
# 문자열 형식지정자에서 %s에 정수를 넣거나, 실수를 넣어도 된다. (암시적 형변환이 되는 것 같다 - 추측)
print('test %s' % 50)  # test 50
print('test %s' % 50.5)  # test 50.5


# 문자열 포맷
print('test {} test'.format("아무거나"))  # test 아무거나 test
print('test {} test {}'.format("아무거나", "넣으세요"))  # test 아무거나 test 넣으세요
# 중괄호 사이에 1, 0 인덱스를 지정해주면 format의 매개변수가 index 사이로 들어간다
print('test {1} test {0}'.format("아무거나", "넣으세요"))  # test 넣으세요 test 아무거나
# 중괄호 사이에 문자열을 넣으면 format의 인자 안에 지정해놓은 문자열과 매칭하여 값이 들어간다
print('test {age} test {color}'.format(age=26, color="black"))  # test 26 test black


# 문자열 포맷 파이썬 v3.6 이상
age = 20
color = "red"
print(f"test {age} test {color}")  # test 20 test red
# 이렇게 나중에 변수를 넣게 되어도 가능하다.
# 근데, 3.9.9 버전에서 시도해보는데 안되는 이유가 뭘까...
# 설정 다 해봤는데 안된다...
print(f"test {age} test {color}")  # test 25 test pink
age = 25  # 나중에 값 넣기
color = "pink"  # 나중에 값 넣기


# 탈출문자 (Escape squence)
print("test n \n")  # \n - 줄바끔
print("test \" and \'")  # "\", \' - 작은, 큰 따옴표
print("test \\")  # \\ - 역슬래쉬
print("test\r r ")  # \r - 커서를 맨 앞으로 이동 - r test
print("test backspace\b")  # 백스페이스 (단어 하나 삭제) - test backspac
print("test \t tab")  # \t - 탭
