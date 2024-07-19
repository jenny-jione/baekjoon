"""
문제 이름: 쉬운 계단 수
문제 링크: https://www.acmicpc.net/problem/10844
문제 티어: 실버 1

타임라인
2024.07.18 11:31am~11:53am (22분)  total: 22분

<정리>
"""

K = 1000000000
n = int(input())
a = [[0]*10 for _ in range(101)]
a[1] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
for i in range(2, n+1):
    a[i][0] = a[i-1][1]
    for j in range(1, 9):
        a[i][j] = (a[i-1][j-1] + a[i-1][j+1]) % K
    a[i][9] = a[i-1][8]
print(sum(a[n]) % K)