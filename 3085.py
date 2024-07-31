"""
문제 이름: 사탕 게임
문제 링크: https://www.acmicpc.net/problem/3085
문제 티어: 실버 2

타임라인
2024.07.29 01:42pm~02:26pm (44분)
2024.07.29 03:10pm~04:00pm (50분)
2024.07.31 08:49am~09:18am (29분)  total: 123분

<정리>
1. 두 값을 swap하는 법
    a, b = b, a
2. 연속하는 최대값 구하는건 그냥 인덱스 0부터 N-1까지 x, x+1을 비교하면 됨.
    x == x+1이면 cnt++ 해주고
    다르면 그 때 한 번 max_cnt값 업데이트 해주고
    0부터 N-1까지 모두 같은 경우가 있으므로 반복문 빠져나온 후에도 한 번 더 업데이트 해주기.
"""

N = int(input())
board = [list(input().rstrip()) for _ in range(N)]

def row_check(r):
    cnt, max_cnt = 1, 0
    for j in range(N-1):
        if board[r][j] == board[r][j+1]:
            cnt += 1
        else:
            if max_cnt < cnt:
                max_cnt = cnt
            cnt = 1
    if max_cnt < cnt:
        max_cnt = cnt
    return max_cnt

def col_check(c):
    cnt, max_cnt = 1, 0
    for i in range(N-1):
        if board[i][c] == board[i+1][c]:
            cnt += 1
        else:
            if max_cnt < cnt:
                max_cnt = cnt
            cnt = 1
    if max_cnt < cnt:
        max_cnt = cnt
    return max_cnt

answer = 0
for i in range(N):
    for j in range(N):
        r, c = row_check(i), col_check(j)
        answer = max(answer, r, c)

for i in range(N):
    for j in range(N-1):
        board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
        answer = max(answer, row_check(i), col_check(j), col_check(j+1))
        board[i][j], board[i][j+1] = board[i][j+1], board[i][j]

for j in range(N):
    for i in range(N-1):
        board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
        answer = max(answer, row_check(i), row_check(i+1), col_check(j))
        board[i][j], board[i+1][j] = board[i+1][j], board[i][j]

print(answer)