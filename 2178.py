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



# 다시 풀기
"""
타임라인
2024.06.13 11:43am~11:56am (13분)
2024.06.13 12:07pm~12:10pm (3분)  total: 16분

<정리>
"""

from collections import deque
N, M = map(int, input().split())
board = []
visited = [[0]*M for _ in range(N)]
for _ in range(N):
    board.append(list(map(int, input())))

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def bfs():
    q = deque([[0, 0]])
    visited[0][0] = 1
    while q:
        y, x = q.popleft()
        if y==N-1 and x==M-1:
            print(visited[N-1][M-1])
            break
        for yi, xi in zip(dy, dx):
            ny, nx = y+yi, x+xi
            if ny not in range(N) or nx not in range(M):
                continue
            if visited[ny][nx]==0 and board[ny][nx]==1:
                visited[ny][nx] = visited[y][x] + 1
                q.append([ny, nx])
                
bfs()