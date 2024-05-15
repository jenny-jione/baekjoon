"""
문제 이름: 알파벳
문제 링크: https://www.acmicpc.net/problem/1987

타임라인
2024.05.10 ~ 2024.05.15

<처음 코드가 시간초과 난 이유>
1. az_check 배열을 지금까지 지나온 A~Z를 저장하는 리스트로 씀. 그래서 매번 in 검사를 해야만 했음
2. visited와 az_check를 각각 설정했는데 그럴 필요가 없었다.
    방문한 좌표인지 검사하는 것 == az_check에 있는 알파벳인지 검사하는 것
    즉 같은 과정을 중복해서 검사하게 됨
3. python3 으로 제출하면 시간초과가 뜸.
4. board에 입력 그대로 알파벳을 저장함

<수정>
1. visited와 az_check를 az라는 크기 26의 배열로 고침.
    ord('A')-65==0이므로 az[0]은 A를 지나왔는지 저장하고, ... az[25]는 Z를 지나왔는지 저장함
2. 1과 동일
3. pypy로 제출하면 통과함..!ㅎ
4. board에 알파벳 말고 0~25로 저장함
"""


R, C = map(int, input().split())
board = []

for _ in range(R):
    line = input().rstrip()
    board.append([ord(l)-65 for l in line])

az = [0] * 26
az[board[0][0]] = 1
answer = 0

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def move_check(ny, nx):
    if ny not in range(R):
        return False
    if nx not in range(C):
        return False
    if az[board[ny][nx]] == 1:
        return False
    return True

def dfs(y, x):
    global answer
    if answer == 26:
        return
    move = False
    for yi, xi in zip(dy, dx):
        ny = y + yi
        nx = x + xi
        if not move_check(ny, nx):
            continue
        az[board[ny][nx]] = 1
        dfs(ny, nx)
        az[board[ny][nx]] = 0
        move = True
    if not move:
        answer = max(answer, sum(az))
        return

dfs(0, 0)
print(answer)