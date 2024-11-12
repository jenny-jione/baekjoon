"""
문제 이름: 나무 자르기
문제 링크: https://www.acmicpc.net/problem/2805
문제 티어: 실버 2

타임라인
2024.11.12 11:29am~12:02pm (33분)
2024.11.12 12:47pm~12:58pm (11분)  total: 44분

<정리>
1. 이분 탐색
"""

import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
trees = list(map(int, input().rstrip().split()))
start, end = 1, max(trees)

while start <= end:
    mid = (start+end) // 2
    tree = 0
    for h in trees:
        if h > mid:
            tree += h - mid
    
    if tree < M:
        end = mid - 1
    else:
        start = mid + 1

print(end)