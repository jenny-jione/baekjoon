"""
문제 이름: 대칭 차집합
문제 링크: https://www.acmicpc.net/problem/1269
문제 티어: 실버 4

타임라인
2024.06.04 02:21pm~02:24pm (3분)
"""

import sys
input = sys.stdin.readline

a, b = map(int, input().strip().split())
s1 = set(map(int, input().strip().split()))
s2 = set(map(int, input().strip().split()))
print(len(s1-s2)+len(s2-s1))