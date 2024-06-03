"""
문제 이름: 좌표 정렬하기
문제 링크: https://www.acmicpc.net/problem/11650
문제 티어: 실버 V

타임라인
2024.06.03 02:30pm~02:38pm (8분)
"""

import sys
input = sys.stdin.readline

N = int(input())
coord = {}
for _ in range(N):
    x, y = map(int, input().rstrip().split())
    coord.setdefault(x, [])
    coord[x].append(y)

for x in sorted(coord.keys()):
    ylist = sorted(coord[x])
    for y in ylist:
        print(x, y)


# 다른 풀이 - 이차원 리스트도 sort 한 번에 정렬됨.
import sys
input = sys.stdin.readline
N = int(input())

coord = []
for _ in range(N):
    coord.append(list(map(int, input().rstrip().split())))
coord.sort()
for x, y in coord:
    print(x, y)