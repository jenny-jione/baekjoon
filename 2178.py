"""
문제 이름: 미로 탐색
문제 링크: https://www.acmicpc.net/problem/2178

타임라인
2024.4.11 9:00am~9:50am (50분)
"""

import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] * M for _ in range(N)]
for i in range(N):
    line = input().rstrip()
    graph[i] = [int(c) for c in line]

visited = [[0] * M for _ in range(N)]

# 우, 좌, 하, 상
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(i, j):
    q = deque([(i, j)])
    visited[i][j] = 1
    while q:
        y, x = q.popleft()
        for yi, xi in zip(dx, dy):
            ny, nx = y+yi, x+xi
            if 0<=ny<N and 0<=nx<M and graph[ny][nx] and not visited[ny][nx]:
                visited[ny][nx] = visited[y][x] + 1
                q.append((ny, nx))
                if ny == N-1 and nx == M-1:
                    return
    return

bfs(0, 0)
print(visited[-1][-1])