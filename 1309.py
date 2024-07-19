"""
문제 이름: 동물원
문제 링크: https://www.acmicpc.net/problem/1309
문제 티어: 실버 1

타임라인
2024.07.19 01:32pm~02:04pm (32분)  total: 32분

<정리>
1. 점화식 세우기.
"""

# 내 풀이
n = int(input())
dp = [[0, 0, 0] for _ in range(n+1)]
dp[1] = [1, 1, 1]
for i in range(2, n+1):
    dp[i][0] = (dp[i-1][0] + dp[i-1][1] + dp[i-1][2]) % 9901
    dp[i][1] = (dp[i-1][0] + dp[i-1][2]) % 9901
    dp[i][2] = (dp[i-1][0] + dp[i-1][1]) % 9901
print(sum(dp[n]) % 9901)


# 다른 풀이
def solve():
    n = int(input())
    if n == 1:
        return 3
    elif n == 2:
        return 7
    dp = [0] * (n+1)
    dp[1] = 3
    dp[2] = 7
    for i in range(3, n+1):
        dp[i] = (dp[i-2] + dp[i-1]*2) % 9901
    return dp[n]

print(solve())


# 다른 풀이를 좀더 예쁘게 고침
def solve():
    n = int(input())
    dp = [1, 3, 7] + [0] * (n-2)
    for i in range(3, n+1):
        dp[i] = (dp[i-2] + dp[i-1]*2) % 9901
    return dp[n]

print(solve())