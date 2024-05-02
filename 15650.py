"""
문제 이름: N과 M (2)
문제 링크: https://www.acmicpc.net/problem/15650

타임라인
2024.04.30 3:37pm~3:42pm (5분)

문제 정리
1. (1 2)는 허용, (2 1)은 허용x --> 조합 문제
"""

N, M = map(int, input().split())

visited = [0] * (N+1)
seq = []

def solve(start):
    if len(seq)==M:
        print(' '.join(map(str, seq)))
        return
    for i in range(start, N+1):
        if not visited[i]:
            visited[i] = 1
            seq.append(i)
            solve(i)
            visited[i] = 0
            seq.pop()

solve(1)