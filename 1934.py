"""
문제 이름: 최소공배수
문제 링크: https://www.acmicpc.net/problem/1934
문제 티어: 브론즈 1

타임라인
2024.06.06 10:31am~11:08am (37분)

<정리>
1. 최소공배수를 구하는 모듈이 있다. math.lcm
2. TODO:근데 이 모듈 쓰지 않고 최소공배수를 구해보자.
"""

# 시간초과.
T = int(input())
def get_lcm(a, b):
    i, j = 1, 1
    while True:
        na, nb = i*a, j*b
        if na==nb:
            return na
        elif na < nb:
            i += 1
        else:
            j += 1

for _ in range(T):
    a, b = map(int, input().split())
    print(get_lcm(a, b))


# math 모듈 써서 통과. 근데 맘에 안듦.
import math
T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    print(math.lcm(a, b))


# math 모듈 안쓰고 -- 진행중
# T = int(input())
# def get_prime_numbers(n):
#     for i in range(1, n+1):