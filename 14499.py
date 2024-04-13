"""
문제 이름: 주사위 굴리기
문제 링크: https://www.acmicpc.net/problem/14499

타임라인
2024.4.13 8:45pm~10:07pm (82분)

이 문제에서 배운 것
1. 주사위와 주사위 굴린 후의 여섯 면을 좌표로 표현하는 방법
2. 꼼꼼해야 할 것
    2-1) 동서북남으로 굴렸을 때 각가의 면이 어디로 가는지 정확히 정의해야 한다.
    2-2) 지도를 벗어날 경우 주사위를 굴리면 안되기 때문에 ny, nx의 범위를 우선 체크해야 한다.
         안그러면 주사위를 먼저 굴려버린 상태로 정보가 업데이트 된다.
"""

import sys
input = sys.stdin.readline

# 위 아 앞 뒤 좌 우
dice = [0]*6
direct = {
    1: [5, 3, 0, 0, -4, -4],
    2: [4, 4, 0, 0, -3, -5],
    3: [3, 1, -2, -2, 0, 0],
    4: [2, 2, -1, -3, 0, 0]
}

# 동 서 북 남
dy = [0, 0, -1, 1]
dx = [1, -1, 0, 0]
tmpdir = ['동', '서', '북', '남']

def move(y, x, od):
    global dice
    # print('order', od, tmpdir[od-1], f'{x},{y}')
    ny, nx = y+dy[od-1], x+dx[od-1]
    if ny not in range(N) or nx not in range(M):
        return (y, x)
    roll_dice = [0]*6
    for i in range(6):
        ni = i+direct[od][i]
        roll_dice[i] = dice[ni]
    dice = [n for n in roll_dice]

    # 지도 칸에 써있는 수
    kan = board[ny][nx]
    if kan == 0:
        board[ny][nx] = dice[1]
    else:
        dice[1] = kan
        board[ny][nx] = 0
    print(dice[0])
    return (ny, nx)

N, M, y, x, K = map(int, input().split())
board = [[] for _ in range(N)]
for i in range(N):
    board[i] = list(map(int, input().split()))
order = list(map(int, input().split()))

for od in order:
    y, x = move(y, x, od)