"""
문제 이름: 색종이
문제 링크: https://www.acmicpc.net/problem/2563
문제 티어: 실버 5

타임라인
2024.07.06 10:29pm~10:54pm (25분)  total: 25분

<정리>
1. 이차원 배열 초기화
2. 겹치는 부분 다루기
"""


N = 100
board = [[0]*N for _ in range(N)]
n = int(input())
answer = 0
for _ in range(n):
    x, y = map(int, input().split())
    for i in range(y, y+10):
        for j in range(x, x+10):
            if board[i][j]==0:
                board[i][j] = 1
                answer += 1
print(answer)