"""
문제 이름: 숫자 카드
문제 링크: https://www.acmicpc.net/problem/10815
문제 티어: 실버 V

타임라인
2024.06.04 10:46am~10:59am (13분)

<정리>
1. if in 할 때, list보다 set이 훨씬 빠르다.
    set은 hash를 사용하기 때문.
    마찬가지로 dict이 훨씬 빠르다.
2. 이진탐색으로 풀면 메모리가 절약된다.
    단 배열이 sort 되어 있어야 함.
"""

# 내 코드 - 269568KB    1020ms
N = int(input())
plus = [0] * 10000001
minus = [0] * 10000001
my_card = list(map(int, input().split()))
for i in my_card:
    if i > 0:
        plus[i] = 1
    else:
        minus[-i] = 1

M = int(input())
cards = list(map(int, input().split()))
for i in cards:
    if i > 0:
        print(plus[i], end=' ')
    else:
        print(minus[-i], end=' ')


# 이진 탐색으로 풀기 - 113096KB	1936ms
N = int(input())
my_card = sorted(list(map(int, input().split())))
M = int(input())
card = list(map(int, input().split()))

def binary_search(target):
    low, high = 0, N-1
    while(low<=high):
        mid = (low+high)//2
        if my_card[mid] == target:
            return 1
        elif my_card[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return 0

for target in card:
    print(binary_search(target), end=' ')