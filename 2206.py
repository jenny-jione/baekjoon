"""
문제 이름: 벽 부수고 이동하기
문제 링크: https://www.acmicpc.net/problem/2206

타임라인
2024.4.11 8:48pm
~2024.4.12 10:40am

배운 것
1. 붙어서 들어오는 입력을 따로따로 저장하려면 list(map(int, input())) 으로 처리하면 된다.
2. 공백과 함께 들어오는 입력을 저장하려면 list(map(int, input().split()))
3. 2차원 배열, 3차원 배열 초기화는 arr[i][j][k] k->j->i 순서로 생각하자!
"""

import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graph = []
for i in range(N):
    graph.append(list(map(int, input().rstrip())))

# 상 하 좌 우
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def bfs():
    q = deque([(0, 0, 0)])
    visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
    visited[0][0][0] = 1
    while q:
        y, x, wall_break = q.popleft()
        if y == N-1 and x == M-1:
            return visited[N-1][M-1][wall_break]
        for yi, xi in zip(dy, dx):
            ny, nx = y+yi, x+xi
            if ny in range(N) and nx in range(M):
                # 벽이면서 그 전에 부순적이 없을 때
                if graph[ny][nx]==1 and wall_break==0:
                    visited[ny][nx][1] = visited[y][x][0] + 1
                    q.append([ny, nx, 1])
                # 방문한 적이 없는 길일 때 
                # 그 전에 벽 부순적 있다면 wall_break==1일 것이고 부순적이 없다면 wall_break==0일 것이므로
                # wall_break의 index 저장은 자동으로 그 직전 정보를 저장하면 된다.
                if graph[ny][nx]==0 and visited[ny][nx][wall_break]==0:
                    visited[ny][nx][wall_break] = visited[y][x][wall_break] + 1
                    q.append([ny, nx, wall_break])
    return -1

print(bfs())

# 내 코드의 흔적.. 2중 for문 안에 bfs까지 넣으면 시간초과가 난다.
# result = []
# res = bfs()
# if res:
#     result.append(res)

# for i in range(N):
#     for j in range(M):
#         if graph[i][j]==1:
#             graph[i][j] = 0
#             res = bfs()
#             print(i, j, res)
#             if res:
#                 result.append(res)
#             graph[i][j] = 1
# if not result:
#     print(-1)
# else:
#     result.sort()
#     print(result)
#     print(result[0])

"""
다시풀기 리뷰 (4.22, 4.30)
q를 y,x만 저장하게 코드를 짜서 또 헤맴..

각 위치마다 wall_break를 같이 저장해둔다는 아이디어가 가장 중요함!!
q에 append할 때 행,열과 함께 wall_break 정보도 같이 append한다.
그래서 popleft할 때마다 wall_break 정보를 가져올 수 있음.

visited 배열과 헷갈리지 말자.
visited는 보통 2차원 배열로 만들어둔 뒤 y,x 위치를 방문했는지 여부를 저장한다.
여기서는 특정 좌표에 도달할 때 벽을 부순 후에 방문했을 수도 있고, 한 번도 부수지 않고 방문했을 수도 있다.
그래서 두 가지 경우를 따로 다뤄야 하기 때문에 visited를 3차원 배열로 만든다.
길(벽이 아닌 곳)의 경우 그 전에 벽을 부쉈는지 부수지 않았는지는 popleft로 얻은 wall_break로 알 수 있다.


지나갈 수 있는 경우는 두 가지임
1. 벽이 아닌 곳일 때 & 방문한 적 없을 때
2. 벽이지만 그 전에 부순적이 없을 때

결론: 또 다시 풀기 @!

"""