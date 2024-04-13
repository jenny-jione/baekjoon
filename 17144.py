"""
문제 이름: 미세먼지 안녕!
문제 링크: https://www.acmicpc.net/problem/17144

타임라인
2024.4.13 9:37am~10:37am (60분)
2024.4.13 11:10am~12:17pm (67분)
2024.4.13 12:57pm~?:??pm (??분)
2024.4.13 2:36pm~3:16pm (40분)
2024.4.13 5:15pm~5:40pm (25분)  total: 192분~
"""

import sys
input = sys.stdin.readline

# 행, 열, 시간(초)
R, C, T = map(int, input().rstrip().split())
graph = [[] * C for _ in range(R)]
aircleaner = []
for i in range(R):
    graph[i] = list(map(int, input().split()))
    if -1 in graph[i]:
        aircleaner.append(i)
(ac1, ac2) = aircleaner

dy = [-1, 1, 0, 0]
dx = [0, 0 , 1, -1]

for t in range(T):
    # 1. 확산
    spread = [[0]*C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if graph[i][j] == -1:
                continue
            givenum = 0
            mine = graph[i][j]//5
            for y, x in zip(dy, dx):
                ny, nx = i+y, j+x
                if ny in range(R) and nx in range(C) and graph[ny][nx]!=-1:
                    givenum += 1
                    spread[ny][nx] += mine
            graph[i][j] = graph[i][j] - (mine * givenum)
    
    for i in range(R):
        for j in range(C):
            if graph[i][j] == -1:
                continue
            graph[i][j] += spread[i][j]

    # 2. 공기청정기
    # 공기청정기 위 (반시계방향)
    ac_up = aircleaner[0]
    for y in range(ac_up-1, 0, -1):
        graph[y][0] = graph[y-1][0]
    for x in range(0, C-1):
        graph[0][x] = graph[0][x+1]
    for y in range(0, ac_up):
        graph[y][C-1] = graph[y+1][C-1]
    for x in range(C-1, 1, -1):
        graph[ac_up][x] = graph[ac_up][x-1]
    graph[ac_up][0] = -1
    graph[ac_up][1] = 0

    # 공기청정기 아래 (시계방향)
    ac_down = aircleaner[1]
    for y in range(ac_down+1, R-1):
        graph[y][0] = graph[y+1][0]
    for x in range(C-1):
        graph[R-1][x] = graph[R-1][x+1]
    for y in range(R-1, ac_down, -1):
        graph[y][C-1] = graph[y-1][C-1]
    for x in range(C-1, 1, -1):
        graph[ac_down][x] = graph[ac_down][x-1]
    graph[ac_down][0] = -1
    graph[ac_down][1] = 0

    dust = 2
    for y in range(R):
        for x in range(C):
            dust += graph[y][x]
    # print(t+1, dust)
print(dust)


"""
내 코드
python3으로 제출하면    - 시간초과
pypy3로 제출하면        - 10% 근처에서 틀렸습니다 뜸 .. ㅠ
""" 
# for t in range(T):
#     # 1. 확산
#     spread = [[0]*C for _ in range(R)]
#     for i in range(R):
#         for j in range(C):
#             if graph[i][j] == -1:
#                 continue
#             givenum = 0
#             mine = graph[i][j]//5
#             for y, x in zip(dy, dx):
#                 ny, nx = i+y, j+x
#                 if ny in range(R) and nx in range(C) and graph[ny][nx]!=-1:
#                     givenum += 1
#                     spread[ny][nx] += mine
#             graph[i][j] = graph[i][j] - (mine * givenum)
    
#     for i in range(R):
#         for j in range(C):
#             if graph[i][j] == -1:
#                 continue
#             graph[i][j] += spread[i][j]
    
#     # 2. 공기청정기 작동
#     move = [[0]*C for _ in range(R)]
#     move[ac1][0] = -1
#     move[ac2][0] = -1

#     for y in range(R):
#         for x in range(C):
#             # 그대로
#             if (y in range(1, ac1) or y in range(ac2+1, R-1)) and x in range(1, C-1):
#                 move[y][x] = graph[y][x]

#             # 1
#             if x==0 and y in range(ac1-1):
#                 move[y+1][x] = graph[y][x]
#             # 7
#             if y in range(ac2, R-1) and x==C-1:
#                 move[y+1][x] = graph[y][x]

#             # 2
#             if y==0 and x in range(1, C):
#                 move[y][x-1] = graph[y][x]
#             # 6
#             if y==R-1 and x in range(1,C ):
#                 move[y][x-1] = graph[y][x]
            
#             # 3
#             if x==C-1 and y in range(1,ac1+1):
#                 move[y-1][x] = graph[y][x]
#             # 5
#             if x==0 and y in range(ac2+2, C):
#                 move[y-1][x] = graph[y][x]
            
#             # 4, 8
#             if y==ac1 and x in range(1, C-1):
#                 move[y][x+1] = graph[y][x]
#             if y==ac2 and x in range(1, C-1):
#                 move[y][x+1] = graph[y][x]
            
#     for i in range(R):
#         graph[i] = copy.deepcopy(move[i])
#     graph[ac1][0] = -1
#     graph[ac2][0] = -1

# dust = 2
# for i in range(R):
#     dust += sum(graph[i])
# print(dust)