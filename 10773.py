"""
문제 이름: 제로
문제 링크: https://www.acmicpc.net/problem/10773
문제 티어: 실버 4

타임라인
2024.06.18 06:00pm~06:08pm (8분)  total: 8분

<정리>
1. 단순한 스택(리스트) append&pop 문제
"""


import sys
input = sys.stdin.readline
li = []
answer = 0
K = int(input().rstrip())
for _ in range(K):
    num = int(input().rstrip())
    if num==0:
        answer -= li.pop()
    else:
        answer += num
        li.append(num)

print(answer)