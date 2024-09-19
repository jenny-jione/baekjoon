"""
문제 이름: 인구 이동
문제 링크: https://www.acmicpc.net/problem/16234
문제 티어: 골드 4

타임라인
2024.09.18 09:56pm~10:10pm (14분)
2024.09.18 10:14pm~10:28pm (14분)  total: 28분

<정리>
"""
from collections import deque

N, L, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def move(union, cnt):
    new_cnt = cnt // len(union)
    for y, x in union:
        board[y][x] = new_cnt

def bfs(y0, x0):
    q = deque([(y0, x0)])
    visited[y0][x0] = 1
    union = []
    cnt = 0
    while q:
        y, x = q.popleft()
        union.append((y, x))
        cnt += board[y][x]
        for yi, xi in zip(dy, dx):
            ny, nx = y+yi, x+xi
            if 0<=ny<N and 0<=nx<N and visited[ny][nx]==0 and L<=abs(board[y][x]-board[ny][nx])<=R:
                q.append((ny, nx))
                visited[ny][nx] = 1
    if len(union) > 1:
        move(union, cnt)
        return True
    else:
        return False
    
answer = 0
while True:
    check = False
    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                if bfs(i, j):
                    check = True
    if check:
        answer += 1
    else:
        break

print(answer)
