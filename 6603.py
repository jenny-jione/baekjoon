"""
문제 이름: 로또
문제 링크: https://www.acmicpc.net/problem/6603
문제 티어: 실버 2

타임라인
2024.08.11 02:11pm~02:17pm (6분)  total: 6분

<정리>
"""
import sys
from itertools import combinations
input = sys.stdin.readline

while True:
    line = list(map(int, input().rstrip().split()))
    k, num = line[0], line[1:]
    if k == 0:
        break
    num.sort()
    for x in combinations(num, 6):
        print(*x)
    print()