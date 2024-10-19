"""
문제 이름: 그림
문제 링크: https://www.acmicpc.net/problem/1926
문제 티어: 실버 1

타임라인
2024.10.18 10:50am~11:10am (20분)  total: 20분

<정리>
1. 그래프 탐색
2. BFS
3. DFS
"""

# 내 코드
from collections import deque

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

def bfs(visited, i, j):
    q = deque([(i, j)])
    visited[i][j] = 1
    size = 1
    while q:
        y, x = q.popleft()
        for yi, xi in zip(dy, dx):
            ny, nx = y+yi, x+xi
            if 0<=ny<n and 0<=nx<m and board[ny][nx]==1 and visited[ny][nx]==0:
                visited[ny][nx] = 1
                size += 1
                q.append((ny, nx))
    return size

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
result = []
for i in range(n):
    for j in range(m):
        if board[i][j] == 1 and visited[i][j]==0:
            result.append(bfs(visited, i, j))
if result:
    result.sort()
    print(len(result))
    print(result[-1])
else:
    print(0)
    print(0)



# 메모리 개선한 코드
from collections import deque

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

def bfs(visited, i, j):
    q = deque([(i, j)])
    visited[i][j] = 1
    area = 1
    while q:
        y, x = q.popleft()
        for yi, xi in zip(dy, dx):
            ny, nx = y+yi, x+xi
            if 0<=ny<n and 0<=nx<m and board[ny][nx]==1 and visited[ny][nx]==0:
                visited[ny][nx] = 1
                area += 1
                q.append((ny, nx))
    return area

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

num_pictures = 0
max_size = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == 1 and visited[i][j]==0:
            num_pictures += 1
            max_size = max(max_size, bfs(visited, i, j))

print(num_pictures)
print(max_size)