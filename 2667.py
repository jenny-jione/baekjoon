"""
문제 이름: 단지번호 붙이기
문제 링크: https://www.acmicpc.net/problem/2667
문제 티어: 실버 1

타임라인
2024.4.10 8:10pm~8:56pm (46분)

<이 문제를 풀면서 얻은 것>
1. 1001011 이렇게 한 줄에 붙어서 들어오는 입력은 input().rstrip()으로 받아서 \n을 없애주자.
    왜냐면 [int(c) for c in line] 을 할 때 int('\n')을 하게 되어서 오류가 난다.
    ValueError: invalid literal for int() with base 10: '\n'
"""

import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
graph = []
for i in range(N):
    # line = input().rstrip()
    line = input()
    graph.append([int(c) for c in line])

visited = [[0] * N for _ in range(N)]
# 우, 좌, 하, 상
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x0, y0):
    global danji
    danji += 1
    q = deque([(x0, y0)])
    house = 0
    visited[x0][y0] = 1
    while q:
        i, j = q.popleft()
        house += 1
        for x, y in zip(dx, dy):
            nx, ny = x+i, y+j
            if 0<=nx<N and 0<=ny<N and graph[nx][ny] and not visited[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = 1
    return house
    
danji = 0
zipnum = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1 and not visited[i][j]:
            res = bfs(i, j)
            zipnum.append(res)
zipnum.sort()

print(danji)
for z in zipnum:
    print(z)



# 다시 풀기
"""
타임라인
2024.06.13 12:18pm~12:29pm (11분)  total: 11분

<정리>
1. 붙어서 들어오는 입력은 그냥 list(map(int, input()))을 해주면 리스트로 저장된다.
"""

from collections import deque

N = int(input())
board = []
for _ in range(N):
    board.append(list(map(int, input())))
visited = [[0]*N for _ in range(N)]
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

danzi = 0
houses = []

def bfs(y, x):
    q = deque([[y, x]])
    visited[y][x] = 1
    cnt = 0
    while q:
        y, x = q.popleft()
        cnt += 1
        for yi, xi in zip(dy, dx):
            ny, nx = y+yi, x+xi
            if ny not in range(N) or nx not in range(N):
                continue
            if visited[ny][nx]==0 and board[ny][nx]==1:
                visited[ny][nx] = 1
                q.append([ny, nx])
    return cnt


for i in range(N):
    for j in range(N):
        if not visited[i][j] and board[i][j]:
            # 단지 탐색 시작
            houses.append(bfs(i, j))
            danzi += 1

houses.sort()
print(danzi)
for h in houses:
    print(h)