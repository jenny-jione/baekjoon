"""
문제 이름: 패션왕 신해빈
문제 링크: https://www.acmicpc.net/problem/9375
문제 티어: 실버 3

타임라인
2024.11.14 12:44pm~12:52pm (8분)  total: 8분

<정리>
1. 조합
2. 경우의 수
3. 딕셔너리 활용
4. dict 대신 collections 모듈의 defaultdict 사용하기
"""

# 내 코드
def solve():
    n = int(input())
    clothes = {}
    for _ in range(n):
        _, kind = input().split()
        clothes.setdefault(kind, 0)
        clothes[kind] += 1
    
    result = 1
    for x in clothes.values():
        result *= (x+1)
    return result - 1

T = int(input())
for _ in range(T):
    print(solve())


# defaultdict를 이용한 코드
from collections import defaultdict

def solve(items):
    clothes = defaultdict(int)
    for _, kind in items:
        clothes[kind] += 1
    
    result = 1
    for count in clothes.values():
        result *= (count+1)
    return result - 1

T = int(input())
for _ in range(T):
    n = int(input())
    items = [input().split() for _ in range(n)]
    print(solve(items))