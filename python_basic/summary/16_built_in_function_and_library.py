# abs, len, range, min, max, pow, reversed, sorted 메서드는 생략

# divmod()
div, mod = divmod(7, 5)
print('divmod: ', div, mod)  # 1 2


# enumerate()
int_list = [1, 2, 3, 4, 5]
for index, element in enumerate(int_list):
    print('enumerate: ', index, element)  # 0 1, 1 2 ...


# eval() - 문자열을 실행하는 메서드. 문자열로 된 수식들을 계산해 주는 간편함이 있지만 취약점이 존재하고 코딩 테스트에 적합하지 않은 메서드
x = 1
result = eval('x + 1')
print('eval: ', result)  # 1


# filter, map
filter_example = filter(lambda x: x % 2 == 0, [1, 2, 3])
map_example = map(lambda x: x * 2, [1, 2, 3])
print('filter: ', list(filter_example))  # 2
print('map: ', list(map_example))  # 2, 4, 6


# zip
zip1 = [1, 2, 3]
zip2 = ["hi", "hello", "good"]
zip_list = list(zip(zip1, zip2))
print('zip: ', zip_list)  # (1, 'hi'), (2, 'hello'), (3, 'good')


# 팩토리얼, 제곱근, 최대공약수 계산
from math import factorial, sqrt, gcd
print('factorial: ', factorial(5))  # 120
print('sqrt: ', sqrt(16))  # 4.0
print('gcd: ', gcd(15, 5))  # 5


# permutation, combination, 중복 순열, 중복 조합
from itertools import permutations, combinations, product, combinations_with_replacement
data = ['A', 'B', 'C']
perm_result = list(permutations(data, 2))
comb_result = list(combinations(data, 2))
print('perm: ', perm_result)  # ('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')
print('comb: ', comb_result)  # ('A', 'B'), ('A', 'C'), ('B', 'C')
data2 = ['a', 'a', 'b', 'b', 'c']
product_result = list(product(data, repeat=2))  # 중복 순열
comb_replace_result = list(combinations_with_replacement(data, 2))  #중복 조합
print('product: ', product_result)
print('comb_with_replacement', comb_replace_result)


# 참고로 갯수를 알고싶다면 itertools가 아닌 math 라이브러리에 있는 perm, comb 메서드를 사용하는 것이 좋다.
from math import perm, comb
perm_count = perm(len(data), 2)
comb_count = comb(len(data), 2)
print('perm count: ', perm_count)  # 6
print('comb count: ', comb_count)  # 3


# Counter
from collections import Counter
counter = Counter([0, 1, 2, 3, 4, 5, 5, 5])
print('counter: ', counter[5])
counter_dict = dict(counter)  # dict로 변환 가능


# deque queue
from collections import deque
queue = deque()
queue.append(1)
queue.appendleft(2)
queue.pop()
queue.popleft()


# defaultdict 딕셔너리 편하게 사용하는 법, 키에 대한 값이 없는 경우 거짓에 해당하는 값을 반환한다. int - 0, str - '', bool - False
from collections import defaultdict
d_dict = defaultdict(int)
d_dict['test'] = 1
print('dict with key: ', d_dict['test'])  # 1 반환
print('dict without key: ', d_dict['no_key'])  # 0 반환


# heapq 최소 힙
import heapq
heap_example = [1, 2, 3, 4, 5]
heapq.heapify(heap_example)  # heap 자료형으로 만들어준다.
heapq.heappush(heap_example, 6)
pop_item1 = heapq.heappop(heap_example)
# push, pop을 개별적으로 수행하는 것보다 2개의 메서드를 사용하는 것이 효율적이다.
pop_item2 = heapq.heapreplace(heap_example, 7)  # 가장 작은 항목을 pop 한 후 값을 넣는다. (값을 넣기 전 pop 한다)
pop_item3 = heapq.heappushpop(heap_example, 8)  # 먼저 값을 push 후 가장 작은 값을 pop 한다.
print('heap pop item: ', pop_item1)
print('heap pop item: ', pop_item2)
print('heap pop item: ', pop_item3)


# bisect 이진탐색
from bisect import bisect_left, bisect_right, bisect
nums = [1, 2, 3, 3, 3, 4, 5]
left_index = bisect_left(nums, 3)  # 값이 들어갈 인덱스를 반환한다. 만약 중복된 값이 있다면 앞쪽(왼쪽) 인덱스를 반환한다.
right_index = bisect_right(nums, 3)  # 값이 들어갈 인덱스를 반환한다. 만약 중복된 값이 있다면 뒷쪽(오른쪽) 인덱스를 반환한다.
left_next_index = bisect(nums, 3)  # bisect_left와 다른 점은 앞이 아닌 뒤의 인덱스를 반환한다. bisect_right와 동일한 함수이다.
print('bisect left index: ', left_index)  # 2
print('bisect right index: ', right_index)  # 5
print('bisect index: ', left_next_index)  # 5
