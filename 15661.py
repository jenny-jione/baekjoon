"""
문제 이름: 링크와 스타트
문제 링크: https://www.acmicpc.net/problem/15661
문제 티어: 골드 5

타임라인
2024.08.13 03:10pm~03:34pm (24분)  total: 24분

<정리>
"""

from itertools import combinations
N = int(input())
s = [list(map(int, input().split())) for _ in range(N)]
answer = int(1e9)

def cal_power(t1: list, t2: list):
    p1, p2 = 0, 0
    for i, j in combinations(t1, 2):
        p1 += s[i][j] + s[j][i]
    for i, j in combinations(t2, 2):
        p2 += s[i][j] + s[j][i]
    return abs(p1-p2)

def solve():
    global answer
    num = [i for i in range(N)]
    for tlen in range(1, N//2+1):
        for x in combinations(num, tlen):
            t1 = list(x)
            t2 = [j for j in range(N) if j not in t1]
            diff = cal_power(t1, t2)
            if diff < answer:
                answer = diff
            if answer == 0:
                return

solve()
print(answer)