"""
문제 이름: 부녀회장이 될테야
문제 링크: https://www.acmicpc.net/problem/2775
문제 티어: 브론즈 1

타임라인
2024.10.16 09:32pm~09:51pm (19분)  total: 19분

<정리>
1. dp
"""

dp = [[0] * 15 for _ in range(15)]
for i in range(1, 15):
    dp[0][i] = i

for a in range(1, 15):
    for b in range(1, 15):
        dp[a][b] = dp[a][b-1] + dp[a-1][b]

T = int(input())
for _ in range(T):
    k = int(input())
    n = int(input())
    print(dp[k][n])