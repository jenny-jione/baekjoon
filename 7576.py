"""
문제 이름: 토마토
문제 링크: https://www.acmicpc.net/problem/7576

타임라인
2024.4.11 10:56am~11:30am (34분)
2024.4.11 1:26am~1:45am (19분) total: 53분

이 문제의 아이디어:
1. 1이 여러개 있을 경우 동시에 진행해야 한다 !
    => 그래서 bfs 시작 전에 전체 그래프의 모든 원소를 돌면서 graph[y][x]==1인 위치들을 먼저 넣어둔다(init)
"""

import sys
from collections import deque
input = sys.stdin.readline

M, N = map(int, input().split())
graph = [[] * M for _ in range(N)]

unripe = 0
for i in range(N):
    graph[i] = list(map(int, input().split()))
    unripe += graph[i].count(0)
    # [질문] 언제는 map만 해도 되고 언제는 list() 해야 되고 .. 무슨 차이인지 모르겠음 !!! 

if unripe==0:
    print(0)
else:
    visited = [[0] * M for _ in range(N)]
    # 상 하 좌 우
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    def bfs(init_arr):
        day = 0
        q = deque()
        q.extend(init_arr)
        while q:
            y, x = q.popleft()
            day = visited[y][x]
            for yi, xi in zip(dy, dx):
                ny, nx = y+yi, x+xi
                if 0<=ny<N and 0<=nx<M and not visited[ny][nx] and graph[ny][nx]==0:
                    visited[ny][nx] = visited[y][x] + 1
                    graph[ny][nx] = 1
                    q.append([ny, nx])
        return day

    init = []
    for i in range(N):
        for j in range(M):
            if graph[i][j]==1 and visited[i][j]==0:
                init.append((i, j))
    day = bfs(init)

    impossible = False
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                impossible = True

    if impossible:
        print(-1)
    else:
        print(day)