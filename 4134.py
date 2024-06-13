"""
문제 이름: 다음 소수
문제 링크: https://www.acmicpc.net/problem/4134
문제 티어: 실버 4

타임라인
2024.06.13 04:01pm~04:18pm (17분)  total: 17분

<정리>
"""

T = int(input())

def is_prime(n):
    if n==1:
        return False
    if n==2:
        return True
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            return False
    return True

def solve(n):
    if n == 0:
        return 2
    while True:
        if is_prime(n):
            return n
        n += 1

for _ in range(T):
    n = int(input())
    print(solve(n))