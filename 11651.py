"""
문제 이름: 좌표 정렬하기 2
문제 링크: https://www.acmicpc.net/problem/11651
문제 티어: 실버 V

타임라인
2024.06.03 03:17pm~03:20pm (3분)
"""

import sys
input = sys.stdin.readline

N = int(input())
coord = []
for _ in range(N):
    x, y = list(map(int, input().rstrip().split()))
    coord.append([y, x])

coord.sort()

for y, x in coord:
    print(x, y)