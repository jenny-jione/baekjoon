"""
문제 이름: 나이순 정렬
문제 링크: https://www.acmicpc.net/problem/10814
문제 티어: 실버 V

타임라인
2024.06.03 04:16pm~04:21pm (5분)

<정리>
1. 리스트를 다중 조건으로 정렬하기
    ex) 첫번째 오름차순, 마지막 오름차순
    li.sort(key=lambda x:(x[0], x[-1]))
    만약 내림차순으로 정렬하고 싶으면 -를 붙이면 된다. lambda x:(x[0], -x[-1])
2. 근데 나이순으로만 정렬해도 됨.
    왜냐면 나이가 같을 경우 이미 리스트에 저장되어 있던 순서로 정렬된다!
    가입한 순으로 다시 정렬할 필요가 없다.
"""

import sys
input = sys.stdin.readline

N = int(input().rstrip())
members = []
for i in range(N):
    age, name = input().rstrip().split()
    members.append((int(age), name, i))
members.sort(key=lambda x:(x[0], x[-1]))

for age, name, _ in members:
    print(age, name)