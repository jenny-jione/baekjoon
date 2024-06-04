"""
문제 이름: 회사에 있는 사람
문제 링크: https://www.acmicpc.net/problem/7785
문제 티어: 실버 5

타임라인
2024.06.04 11:45am~11:53am (8분)

<정리>
1. dict에서 기억할 것
    1) del
    2) dic.keys()
2. sorted는 반환값이 리스트이다.
3. sys.stdin.readline을 하면 시간이 1/10으로 줄어든다.
"""

n = int(input())
office = {}
for _ in range(n):
    name, stat = input().split()
    office.setdefault(name, '')
    office[name] = stat
li = []
for p, s in office.items():
    if s == 'enter':
        li.append(p)
li.sort(reverse=True)
for p in li:
    print(p)

# del 쓰기
import sys
input = sys.stdin.readline

n = int(input())
office = {}

for _ in range(n):
    name, stat = input().split()
    if stat == 'enter':
        office[name] = stat
    else:
        del office[name]

li = sorted(office.keys(), reverse=True)
for p in li:
    print(p)