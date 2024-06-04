"""
문제 이름: 듣보잡
문제 링크: https://www.acmicpc.net/problem/1764
문제 티어: 실버 4

타임라인
2024.06.04 02:03pm~02:11pm (8분)

<정리>
1. 교집합 - set을 사용하자
2. set
    교집합: & 또는 .intersection()
    합집합: | 또는 .union()
    차집합: - 또는 .difference()
"""

import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())
dic = {}
for _ in range(N+M):
    name = input().strip()
    dic.setdefault(name, 0)
    dic[name] += 1

li = []
for k, v in dic.items():
    if v == 2:
        li.append(k)

li.sort()
print(len(li))
for l in li:
    print(l)


# set 이용하기
import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())
s1 = set()
s2 = set()

for _ in range(N):
    s1.add(input().strip())

for _ in range(M):
    s2.add(input().strip())

result = sorted(list(s1&s2))
print(len(result))
for r in result:
    print(r)