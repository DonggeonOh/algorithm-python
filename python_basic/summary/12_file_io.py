# 파일 입출력
# 파일 쓰기
score_file = open('score.txt', 'w', encoding='utf8')  # 쓰기 권한으로 score.txt 파일을 연다. 없으면 만든다.
print('국어 : 100', file=score_file)  # score.txt 파일에 해당 내용을 쓴다.
print('수학 : 100', file=score_file)
print('영어 : 100', file=score_file)
score_file.close()


# 파일 이어 작성하기
score_file2 = open('score.txt', 'a', encoding='utf8')  # a - append의 의미로 이미 있는 파일에 계속해서 이어 쓰고 싶을 때 사용
score_file2.write('과학 : 100\n')  # score.txt 파일에 과학 : 100 내용을 쓰고 개행한다.
score_file2.close()


# 파일 통째로 읽기
score_file3 = open('score.txt', 'r', encoding='utf8')
print(score_file3.read())


# 파일 한 줄씩 읽기
score_file4 = open('score.txt', 'r', encoding='utf8')
while True:
    line = score_file4.readline()
    if not line:
        break
    print(line, end='')  # 파일을 line 만 읽음
score_file4.close()


# 파일 한 줄씩 리스트에 저장해서 읽기
score_file5 = open('score.txt', 'r', encoding='utf8')
lines = score_file5.readlines()
print()
for line in lines:
    print(line, end='')
score_file5.close()
