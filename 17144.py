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


# 다시풀기 5.30
"""
2024.05.30 11:01am~12:04pm (63분)
2024.05.30 12:27pm~12:43pm (16분)

이 문제에서 배운 것/느낀 점
1. index 다루기 연습을 해야 함. 정확도가 매우 매우 매우 중요함!
    특히 경계값, 모서리에서 더더욱 중요함
2. range 역순일 때  @@ 매 우 주 의 @@
3. range 역순이 어렵다면 reversed를 쓰면 간편하다.
    start값과 끝값만 제대로 설정한 다음 reversed를 적용하면 됨.
    ex. 10부터 0까지 역순으로 출력하고 싶을 때
        => range(10, -1, -1)
        => reversed(range(0, 11))
    ex. R-2부터 cc까지 역순으로 출력하고 싶을 때 (0<cc<R-2)
        => range(R-2, cc-1, -1) 
        => reversed(range(cc, R-1))
        
"""
import math

R, C, T = map(int, input().split())
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
room = []
ac = []
for i in range(R):
    room.append(list(map(int, input().split())))
    if room[-1][0] == -1:
        ac.append(i)
aa, cc = ac

def spread():
    temp = [[0]*C for _ in range(R)]
    for y in range(R):
        for x in range(C):
            if room[y][x] == -1:
                continue
            cnt = 0
            for yi, xi in zip(dy, dx):
                ny, nx = y+yi, x+xi
                if 0<=ny<R and 0<=nx<C and room[ny][nx]!=-1:
                    temp[ny][nx] += math.floor(room[y][x]/5)
                    cnt += 1
            room[y][x] -= math.floor(room[y][x]/5) * cnt
    for y in range(R):
        for x in range(C):
            room[y][x] += temp[y][x]

def air_cleaning():
    # 반시계
    for y in range(aa-1, -1, -1):
        room[y+1][0] = room[y][0]
    for x in range(1, C):
        room[0][x-1] = room[0][x]
    for y in range(1, aa+1):
        room[y-1][C-1] = room[y][C-1]
    for x in range(C-2, -1, -1):
        room[aa][x+1] = room[aa][x]
    # 시계
    for y in range(cc+1, R):
        room[y-1][0] = room[y][0]
    for x in range(1, C):
        room[R-1][x-1] = room[R-1][x]
    for y in range(R-2, cc-1, -1):
        room[y+1][C-1] = room[y][C-1]
    for x in range(C-2, -1, -1):
        room[cc][x+1] = room[cc][x]
    room[aa][0], room[cc][0] = -1, -1
    room[aa][1], room[cc][1] = 0, 0

for _ in range(T):
    spread()
    air_cleaning()

answer = 2
for i in range(R):
    answer += sum(room[i])
print(answer)