"""
문제 이름: 커트라인
문제 링크: https://www.acmicpc.net/problem/25305
문제 티어: 브론즈 2

타임라인
2024.06.03 11:33am~11:36am (3분)
"""

import sys
input = sys.stdin.readline

N, k = map(int, input().split())
grade = [g for g in map(int, input().strip().split())]
grade.sort(reverse=True)
print(grade[k-1])