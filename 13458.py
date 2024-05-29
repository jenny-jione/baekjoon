"""
문제 이름: 시험 감독
문제 링크: https://www.acmicpc.net/problem/13458

타임라인
2024.05.29 11:57am~12:17pm (20분)

<정리>
1. 시험장의 인원보다 B(총감독관의 감시가능인원)가 클 경우 바로 다음 시험장으로 넘어가야 한다.
    안그러면 음수 몫을 구하게 되어서 틀림
    if vice == 0: (no!)
    if vice <= 0: (yes)
"""

import sys
input = sys.stdin.readline

n = int(input())
classroom = list(map(int, input().strip().split()))
b, c = map(int, input().split())

answer = n
for cr in classroom:
    vice = cr-b
    if vice <= 0:
        continue
    answer += (vice//c)
    if vice%c>0:
        answer += 1
print(answer)
