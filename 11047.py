"""
문제 이름: 동전 0
문제 링크: https://www.acmicpc.net/problem/11047
문제 티어: 실버 4

타임라인
2024.07.02 04:22pm~04:28pm (6분)  total: 6분
"""


coins = []
N, K = map(int, input().split())
for _ in range(N):
    coins.append(int(input()))

left = K
idx = len(coins) - 1
count = 0
while (left>0):
    if coins[idx] <= left:
        count += left//coins[idx]
        left -= coins[idx]*(left//coins[idx])
    else:
        idx -= 1
print(count)