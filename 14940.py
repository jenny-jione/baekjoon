"""
문제 이름: 쉬운 최단거리
문제 링크: https://www.acmicpc.net/problem/14940
문제 티어: 실버 1

타임라인
2024.11.12 02:43pm~03:00pm (17분)  total: 17분

<정리>
1. bfs
2. 문제 조건을 제대로 읽고 정확히 구현해야 한다!!
    갈 수 없는 땅 (0)을 입력단계에서 처리해서 dist에 0으로 업데이트를 해야 함.
    이걸 bfs 단계에서 한다면, 0으로 가로막힌 0은 -1로 남아있게 되어서 틀린다.
"""

from collections import deque

n, m = map(int, input().split())
board = []
dist = [[-1] * m for _ in range(n)]
for i in range(n):
    board.append(list(map(int, input().split())))
    for j in range(m):
        if board[i][j] == 2:
            gy, gx = i, j
        if board[i][j] == 0:
            dist[i][j] = 0

q = deque([(gy, gx)])
dist[gy][gx] = 0
dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]
while q:
    y, x = q.popleft()
    for yi, xi in zip(dy, dx):
        ny, nx = y+yi, x+xi
        if 0<=ny<n and 0<=nx<m and board[ny][nx]!=0 and dist[ny][nx]==-1:
                dist[ny][nx] = dist[y][x] + 1
                q.append((ny, nx))

for i in range(n):
    print(*dist[i])


"""
5 5
1 0 1 0 1
1 0 1 0 1
1 0 2 0 1
1 1 0 1 1
1 1 1 1 1

2 2
2 1
1 0
"""