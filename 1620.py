"""
문제 이름: 나는야 포켓몬 마스터 이다솜
문제 링크: https://www.acmicpc.net/problem/1620
문제 티어: 실버 4

타임라인
2024.06.04 12:04pm~12:13pm (9분)

<정리>
1. '문자열'.isdigit()는 문자열이 숫자로만 이루어져 있는지 확인하는 함수이다.
2. poke와 mon를 따로 선언하는게 아니라 딕셔너리 하나만 선언해서 사용해도 되는 거였음! 너무 복잡하게 생각했다.
    그냥 번호:이름, 이름:번호로 한번씩 저장하면 훨씬 간단해짐.
"""

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
poke = {}
mon = [[] for _ in range(N+1)]
for i in range(1, N+1):
    m = input().strip()
    poke[m] = i
    mon[i] = m

for i in range(M):
    q = input().strip()
    if q.isdigit():
        print(mon[int(q)])
    else:
        print(poke[q])


# 딕셔너리 하나로만 개선한 코드
import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())
poke = {}
for i in range(1, N+1):
    m = input().strip()
    poke[m] = i
    poke[i] = m

for i in range(M):
    q = input().strip()
    if q.isdigit():
        print(poke[int(q)])
    else:
        print(poke[q])