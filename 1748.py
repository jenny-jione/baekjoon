"""
문제 이름: 수 이어 쓰기 1
문제 링크: https://www.acmicpc.net/problem/
문제 티어: 실버 4

타임라인
2024.07.26 01:55pm~02:14pm (19분)  total: 19분

<정리>
"""

N = input()
d = len(N)
n = int(N)

answer = d * (n - 10**(d-1) + 1)
for i in range(d-1):
    answer += (i+1) * (10**(i+1)-10**i)
print(answer)
