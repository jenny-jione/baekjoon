"""
< itertools 공부 >
1. combinations()
2. combinations_with_replacement()
3. permutations()
4. product()
"""

"""
1. combinations(iterable, r)
    : iterable에서 원소 개수가 r개인 조합 뽑기
    : 여기서 조합은 순서를 고려하지 않는다.
"""
from itertools import combinations

arr = [1, 2, 3]

for i in combinations(arr, 2):
    print(i)

'''
출력 결과:
(1, 2)
(1, 3)
(2, 3)
'''


"""
2. combinations_with_replacement(iterable, r)
    : iterable에서 원소 개수가 r개인 중복 조합 뽑기
    : 여기서 조합은 순서를 고려하지 않는다.
    : 중복된 요소를 포함할 수 있다.
"""
from itertools import combinations_with_replacement

arr = ['A', 'B', 'C']

for i in combinations_with_replacement(arr, 2):
    print(i)

'''
출력 결과:
('A', 'A')
('A', 'B')
('A', 'C')
('B', 'B')
('B', 'C')
('C', 'C')
'''


"""
3. permutations(iterable, r=None)
    : iterable에서 원소 개수가 r개인 순열 뽑기
    : 여기서 순열은 순서를 고려한다.
    : r을 지정하지 않거나 r을 None으로 하면 최대 길이(len(arr))의 순열이 리턴된다.
"""

from itertools import permutations

arr = ['A', 'B', 'C']

for i in permutations(arr):
    print(i)

'''
출력 결과:
('A', 'B', 'C')
('A', 'C', 'B')
('B', 'A', 'C')
('B', 'C', 'A')
('C', 'A', 'B')
('C', 'B', 'A')
'''


"""
4. product(*iterables, repeat=1)
    : 여러 iterable의 데카르트곱(카티션 곱, Cartesian product) 리턴
    : 여러 iterable간의 모든 짝을 지어서 리턴한다.
    : repeat 인자를 사용하면 동일한 iterable을 여러 번 반복해서 조합할 수 있다.
"""

from itertools import product

arr1 = ['A', 'B']
arr2 = ['1', '2']

# arr1과 arr2의 모든 짝을 리턴한다
for i in product(arr1, arr2, repeat=1):
    print(i)

'''
출력 결과:
('A', '1')
('A', '2')
('B', '1')
('B', '2')
'''

# product(arr1, arr1, repeat=1)과 동일. arr1끼리의 모든 찍을 리턴한다
for i in product(arr1, repeat=2):
    print(i)

'''
출력 결과:
('A', 'A')
('A', 'B')
('B', 'A')
('B', 'B')
'''

# product(arr1, arr1, arr1, repeat=1)과 동일.
for i in product(arr1, repeat=3):
    print(i)

'''
출력 결과:
('A', 'A', 'A')
('A', 'A', 'B')
('A', 'B', 'A')
('A', 'B', 'B')
('B', 'A', 'A')
('B', 'A', 'B')
('B', 'B', 'A')
('B', 'B', 'B')
'''