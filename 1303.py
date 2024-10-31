"""
문제 이름: 전쟁 - 전투
문제 링크: https://www.acmicpc.net/problem/1303
문제 티어: 실버 1

타임라인
2024.10.31 09:50am~10:08am (18분)  total: 18분

<정리>
1. bfs
2. dictionary로 저장하기
3. dict.values()
"""

from collections import deque

N, M = map(int, input().split())
board = [list(input()) for _ in range(M)]
visited = [[0] * N for _ in range(M)]

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]
power = {'W': 0, 'B':0}

def bfs(i, j, color):
    q = deque([[i, j]])
    visited[i][j] = 1
    cnt = 1
    while q:
        y, x = q.popleft()
        for yi, xi in zip(dy, dx):
            ny, nx = y+yi, x+xi
            if 0<=ny<M and 0<=nx<N and board[ny][nx]==color and visited[ny][nx]==0:
                visited[ny][nx] = 1
                cnt += 1
                q.append([ny, nx])
    power[color] += cnt**2
    return

for i in range(M):
    for j in range(N):
        if visited[i][j]==0:
            bfs(i, j, board[i][j])

print(*power.values())