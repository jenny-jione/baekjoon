"""
문제 이름: 타일 채우기
문제 링크: https://www.acmicpc.net/problem/2133
문제 티어: 골드 4

타임라인
2024.07.22 03:37pm~04:24pm (47분)  total: 47분

<정리>
1. 점화식 세우기 - unique를 찾는다!
2. 필요없는 반복문을 돌지 않게 조건문을 잘 세우자.
    n이 홀수일 경우 그 전에 조건문을 작성해서 for문에 아예 들어가지 않게 하자.
"""


n = int(input())
dp = [0, 0, 3] + [0] * (n-2)
for i in range(4, n+1, 2):
    dp[i] = dp[i-2] * 3
    for j in range(4, i, 2):
        dp[i] += dp[i-j] * 2
    dp[i] += 2
print(dp[n])

# 개선한 코드
n = int(input())
dp = [0] * (n+1)
if n % 2 == 1:
    print(0)
else:
    for i in range(4, n+1, 2):
        dp[i] = dp[i-2] * 3
        for j in range(4, i, 2):
            dp[i] += dp[i-j] * 2
        dp[i] += 2
    print(dp[n])
