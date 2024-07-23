"""
문제 이름: 합분해
문제 링크: https://www.acmicpc.net/problem/2225
문제 티어: 골드 5

타임라인
2024.07.23 11:06am~11:29am (23분)  total: 23분

<정리>
"""

n, k = map(int, input().split())
dp = [[0]*(n) for _ in range(k)]

for i in range(k):
    for j in range(n):
        if j==0:
            dp[i][j] = i+1
        elif i==0:
            dp[i][j] = 1
        else:
            dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % 1000000000
print(dp[k-1][n-1])