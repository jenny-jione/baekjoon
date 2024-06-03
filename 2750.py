"""
문제 이름: 수 정렬하기
문제 링크: https://www.acmicpc.net/problem/2750
문제 티어: 브론즈 2

타임라인
2024.06.03 11:18am~11:21am (3분)
"""

import sys
input = sys.stdin.readline

N = int(input())
nums = []
for _ in range(N):
    nums.append(int(input()))

nums.sort()

for n in nums:
    print(n)