"""
문제 이름: 절대힙
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