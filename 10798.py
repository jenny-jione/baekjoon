"""
문제 이름: 세로읽기
문제 링크: https://www.acmicpc.net/problem/10798
문제 티어: 브론즈 1

타임라인
2024.07.05 11:13pm~11:20pm (7분)  total: 7분

<정리>
1. 2차원 배열 초기화
2. a.replace()를 하면 왜 a가 안바뀌는 것 같은지?
"""

board = [[] for _ in range(5)]
for i in range(5):
    board[i] = list(input().ljust(15))

answer = ''
for i in range(15):
    for j in range(5):
        if board[j][i]!=' ':
            answer += board[j][i]

print(answer)