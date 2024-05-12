# 시간초과 해결하기

R, C = map(int, input().split())
visited = [[0] * C for _ in range(R)]
visited[0][0] = 1
board = []
for _ in range(R):
    line = input().rstrip()
    board.append([l for l in line])
az_check = [board[0][0]]
answer = 0

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def move_check(ny, nx):
    if ny not in range(R):
        return False
    if nx not in range(C):
        return False
    if visited[ny][nx]:
        return False
    if board[ny][nx] in az_check:
        return False
    return True

def dfs(y, x):
    global answer
    # print(f'visit {y},{x} -- {board[y][x]}')
    if answer == 26:
        return
    move = False
    for yi, xi in zip(dy, dx):
        ny = y + yi
        nx = x + xi
        if not move_check(ny, nx):
            continue
        visited[ny][nx] = 1
        az_check.append(board[ny][nx])
        dfs(ny, nx)
        visited[ny][nx] = 0
        az_check.pop()
        move = True
    if not move:
        # print(f'{y},{x} ({board[y][x]}) no move! -- from now:', len(az_check))
        answer = max(answer, len(az_check))
        return

dfs(0, 0)
print(answer)