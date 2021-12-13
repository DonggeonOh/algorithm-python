# if문 선언 및 활용
weather = 'rain'
if weather == 'rain':  # is 는 == 과 같다.
    print('Take your umbrella.')
elif weather == 'sunny':
    print('Sunny outside')
else:
    print('Need anything')

temperature = 30
if temperature <= 20:
    print('Cold')
elif 20 < temperature and temperature <= 40:  # 20 < temperature <= 40 과 같다
    print('Wind')
else:
    print('Hot')

compare = 20
if compare < 20:
    pass
else:
    print("{0} is bigger than 20".format(compare))

# for 선언 및 활용
for_example = [1, 2, 3, 4, 5]
for element in for_example:
    print(element, end=" ")
print()
for index in range(5):  # range() 활용
    print(for_example[index], end=" ")
print()
for index in range(2, 5):
    print(for_example[index], end=" ")
print()
tuples = [(1, 2), (3, 4), (5, 6)]
for element in tuples:
    print(element)
for (first, last) in tuples:
    print("tuple[0]: {0} tuple[1]: {1}".format(first, last))
# 리스트 내포 사용하기
a = [1, 2, 3, 4]
b = [num * 3 for num in a]  # a의 리스트를 돌면서 해당 값을 * 3 하여 b에 넣는다 - 결과: [3, 6, 9, 12]
print(b)
# for문으로 a리스트를 돌면서 a의 값이 짝수인 경우에만 해당 값에 2를 곱하여 c 리스트에 넣는다.
c = [num * 2 for num in a if num % 2 == 0]  # 결과: [4, 8]
print(c)
# 리스트 내포를 통해서 구구단 출력하기
d = [x * y for x in range(2, 10)
     for y in range(1, 10)]
print(d)


# while문 선언 및 활용
while_num = 0
while while_num <= 5:
    print(while_num, end=" ")
    while_num += 1
print()
while True:
    if while_num == 10:
        break
    print(while_num, end=" ")
    while_num += 1
print()
