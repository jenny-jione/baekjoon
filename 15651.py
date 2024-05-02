"""
문제 이름: N과 M (3)
문제 링크: https://www.acmicpc.net/problem/15651

타임라인
2024.04.30 3:45pm~3:50pm (5분)

문제 정리
1. 중복순열
"""


N, M = map(int, input().split())
seq = []

def solve():
    if len(seq)==M:
        print(' '.join(map(str, seq)))
        return
    for i in range(1, N+1):
        seq.append(i)
        solve()
        seq.pop()

solve()