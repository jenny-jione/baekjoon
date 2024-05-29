"""
문제 이름: 로봇 청소기
문제 링크: https://www.acmicpc.net/problem/14503

타임라인
2024.05.29 02:21pm~02:57pm (36분)
2024.05.29 03:20pm~03:40pm (20분)

<이 문제에서 배운 것>
1. 시계방향 회전과 반시계방향 회전을 반대로 착각하지 말기! 꼭 정확하게 확인하고 코드를 짜자.
    이번에 첫번째 작성에서 다 맞았다고 생각했는데 시계방향으로 작성해서 틀림.. 그거 고쳐서 바로 맞음
2. 회전하거나 후진할 때 index를 벗어날 수 있으므로 %4를 해주자.
    북 동 남 서 기준으로,
        1) 반시계 방향 90도 회전: (d+3)%4
            북->서, 서->남, 남->동, 동->북 이어서 -1를 하면 되지만,
            음수가 될 수 있으므로 3을 더한 뒤 %4를 해준다.
        2) 후진: (d+2)%4
            북<->남, 동<->서 index 2 차이이므로
"""

N, M = map(int, input().split())
r, c, d = map(int, input().split())
# d : 0 1 2 3 : 북 동 남 서
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

room = []

for _ in range(N):
    room.append(list(map(int, input().split())))

answer = 0
y, x = r, c

while True:
    # 1. 현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소한다.
    if room[y][x] == 0:
        room[y][x] = 7
        answer += 1
    
    # 주변 4칸 청소여부 확인
    near = False
    for yi, xi in zip(dy, dx):
        ny, nx = y+yi, x+xi
        # if ny in range(1, N-1) and nx in range(1, M-1) and room[ny][nx]==0:
        # **풀고 나서 다시 보니까, range(1, N-1)과 room[ny][nx]==0 확인은 겹치는 부분이 있어서 불필요. 왜냐면 room의 맨 가장자리는 항상 1이기 때문에.
        if ny in range(N) and nx in range(M) and room[ny][nx]==0:
            near = True
    
    # 2. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우,
    if not near:
        backy, backx = y+dy[(d+2)%4], x+dx[(d+2)%4]
        if backy in range(N) and backx in range(M):
            # 2-1. 바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면 한 칸 후진한다.
            if room[backy][backx] != 1:
                y, x = backy, backx
            # 뒤쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춘다.
            else:
                break
    # 3. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우,
    else:
        # 반시계 방향으로 90도 회전한다.
        d = (d+3)%4
        fronty, frontx = y+dy[d], x+dx[d]
        if fronty in range(N) and frontx in range(M) and room[fronty][frontx]==0:
            y, x = fronty, frontx

print(answer)