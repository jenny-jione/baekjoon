"""
문제 이름: 나이트의 이동
문제 링크: https://www.acmicpc.net/problem/7562

타임라인
2024.4.11 3:07pm~3:40pm (33분)
"""

import sys
from collections import deque
input = sys.stdin.readline

dy = [-2, -1, 1, 2, 2, 1, -1, -2]
dx = [1, 2, 2, 1, -1, -2, -2, -1]

def bfs(y0, x0, y1, x1, visited):
    q = deque([(y0, x0)])
    while q:
        y, x = q.popleft()
        for yi, xi in zip(dy, dx):
            ny, nx = y+yi, x+xi
            if 0<=ny<L and 0<=nx<L and not visited[ny][nx]:
                visited[ny][nx] = visited[y][x] + 1
                if ny == y1 and nx == x1:
                    return visited[ny][nx]
                q.append((ny, nx))

T = int(input())

for _ in range(T):
    L = int(input())
    graph = [[] * L for _ in range(L)]
    visited = [[0] * L for _ in range(L)]
    s1, s2 = map(int, input().split())
    e1, e2 = map(int, input().split())
    if s1 == e1 and s2 == e2:
        print(0)
    else:
        print(bfs(s1, s2, e1, e2, visited))
