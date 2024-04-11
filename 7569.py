"""
문제 이름: 토마토(3차원)
문제 링크: https://www.acmicpc.net/problem/7569

타임라인
2024.4.11 2:10pm~2:50pm (40분)

이 문제의 포인트
1. 3차원 그래프를 초기화하는 과정
2. 앞뒤좌우상하 dx, dy, dz 리스트
3. 헷갈리지 않고 인덱스 할당하기
"""

import sys
from collections import deque
input = sys.stdin.readline

M, N, H = list(map(int, input().split()))
graph = [[[] * M for _ in range(N)] for _ in range(H)]
visited = [[[0] * M for _ in range(N)] for _ in range(H)]

unripe = 0
for z in range(H):
    for y in range(N):
        graph[z][y] = list(map(int, input().split()))
        unripe += graph[z][y].count(0)

if unripe == 0:
    print(0)
else:
    # 앞 뒤 좌 우 상 하
    dx = [0, 0, -1, 1, 0, 0]
    dy = [1, -1, 0, 0, 0, 0]
    dz = [0, 0, 0, 0, 1, -1]

    def bfs(init_arr):
        day = 0
        q = deque()
        q.extend(init_arr)
        while q:
            z, y, x = q.popleft()
            day = visited[z][y][x]
            for zi, yi, xi in zip(dz, dy, dx):
                nz, ny, nx = z+zi, y+yi, x+xi
                if 0<=nz<H and 0<=ny<N and 0<=nx<M and graph[nz][ny][nx]==0 and not visited[nz][ny][nx]:
                    graph[nz][ny][nx] = 1
                    visited[nz][ny][nx] = visited[z][y][x] + 1
                    q.append((nz, ny, nx))
        return day
    
    # init
    init = []
    for z in range(H):
        for y in range(N):
            for x in range(M):
                if graph[z][y][x] == 1:
                    init.append((z, y, x))
    res = bfs(init)

    impossible = False
    for z in range(H):
        for y in range(N):
            if 0 in graph[z][y]:
                impossible = True
                break
    if impossible:
        print(-1)
    else:
        print(res)