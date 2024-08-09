"""
문제 이름: 가장 긴 증가하는 부분 수열
문제 링크: https://www.acmicpc.net/problem/11053
문제 티어: 실버 2

타임라인
2024.08.09 01:28pm~02:03pm (35분)  total: 35분

<정리>
"""

n = int(input())
a = list(map(int, input().split()))
dp = [1] * n
for i in range(1, n):
    for j in range(i-1, -1, -1):
        if a[j] < a[i]:
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))