"""
문제 이름: 가로수
문제 링크: https://www.acmicpc.net/problem/2485
문제 티어: 실버 4

타임라인
2024.06.13 03:44pm~03:54pm (10분)  total: 10분

<정리>
1. 최대공약수.
"""
import math
N = int(input())
a = int(input())
distance = []
for _ in range(N-1):
    b = int(input())
    distance.append(b-a)
    a = b
interval = math.gcd(*distance)
answer = 0
for d in distance:
    answer += (d//interval)-1
print(answer)