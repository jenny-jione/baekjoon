"""
문제 이름: 절댓값 힙
문제 링크: https://www.acmicpc.net/problem/11286

타임라인
2024.4.8 6:55pm~7:29pm (34분)
2024.4.8 8:28pm~9:15pm (47분)
2024.4.8 9:24pm~9:40pm 못풀어서 정답 봄 ..

새로 알게된 것
1) 우선순위 큐 heapq
2) sys.stdin.readline()도
3) abs !!! 이거 math 모듈인줄 알고 처음에 뚝딱댐..ㅎ 
"""

import sys
import heapq

n = int(input())
q = []

size = 0
for _ in range(n):
    x = int(sys.stdin.readline())
    if x != 0:
        heapq.heappush(q, (abs(x), x))
    else:
        if not q:
            print(0)
        else:
            print(heapq.heappop(q)[1])



"""
복습 (다시 풀어봄)
2024.4.17 수요일

<오늘 정리>
1. heapq.heappush(q, value)
    value에는 튜플 등도 가능하다.
    단, 가장 첫번째 값을 기준으로 정렬된다. (오름차순)
2. 시간초과 원인
    input = sys.stdin.readline 을 해주지 않았음
"""

import heapq
import sys
input = sys.stdin.readline

N = int(input())
q = []
result = []
for _ in range(N):
    x = int(input())
    if x!=0:
        heapq.heappush(q, (abs(x), x))
    else:
        if not q:
            result.append(0)
        else:
            (absval, val) = heapq.heappop(q)
            result.append(val)

for val in result:
    print(val)