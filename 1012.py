"""
문제 이름: 유기농 배추
문제 링크: https://www.acmicpc.net/problem/1012

타임라인
2024.4.11 12:28am~1:32am (64분)
"""

import sys
from collections import deque
input = sys.stdin.readline

def bfs22(i, j, visited):
    q = deque([(i, j)])
    global cnt
    cnt += 1
    while q:
        y, x = q.popleft()
        for d1, d2 in zip(dx, dy):
            ny, nx = y+d2, x+d1
            if 0<=nx<M and 0<=ny<N and graph[ny][nx] and not visited[ny][nx]:
                q.append([ny, nx])
                visited[ny][nx] = 1

T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())
    graph = [[0] * M for _ in range(N)]
    visited = [[0] * M for _ in range(N)]

    # 우, 좌, 상, 하
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]

    for _ in range(K):
        i, j = map(int, input().split())
        graph[j][i] = 1
    
    cnt = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] and not visited[i][j]:
                bfs22(i, j, visited)
    print(cnt)