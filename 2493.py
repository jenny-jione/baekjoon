"""
문제 이름: 탑
문제 링크: https://www.acmicpc.net/problem/2493
문제 티어: 골드 5

타임라인
2024.10.14 01:31pm~02:05pm (34분)  total: 34분

<정리>
1. 스택
2. 스택을 pop하는 조건을 잘 설정해야 한다
"""

import sys
input = sys.stdin.readline

N = int(input())
tower = list(map(int, input().rstrip().split()))

result = [0] * N
s = []
for i in range(N-1, -1, -1):
    if s and tower[i] >= tower[s[-1]]:
        while s:
            if tower[i] < tower[s[-1]]:
                break
            twi = s.pop()
            result[twi] = i+1
    s.append(i)

print(*result)