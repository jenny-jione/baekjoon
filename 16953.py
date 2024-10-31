"""
문제 이름: A -> B
문제 링크: https://www.acmicpc.net/problem/16953
문제 티어: 실버 2

타임라인
2024.10.31 10:14am~10:26am (12분)  total: 12분

<정리>
1. bfs
2. nx를 q에 넣을 때, 조건 개선
    if nx <= int(1e9): 라고 풀었는데,
    if nx <= b: 로 탐색 공간을 줄일 수 있음. 어차피 nx가 b를 넘어가는 경로는 답이 아님.
"""

from collections import deque

def bfs(a, b):
    q = deque([(a, 0)])
    while q:
        x, cnt = q.popleft()
        if x == b:
            return cnt + 1
        for nx in (x*2, x*10+1):
            if nx <= b:
                q.append((nx, cnt+1))
    return -1

a, b = map(int, input().split())
print(bfs(a, b))