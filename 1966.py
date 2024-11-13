"""
문제 이름: 프린터 큐
문제 링크: https://www.acmicpc.net/problem/1966
문제 티어: 실버 3

타임라인
2024.11.13 03:20pm~03:41pm (21분)  total: 21분

<정리>
1. 덱
    q = deque([1, 2, 3, 4, 5])
    q.rotate(-1)
    # q = [2, 3, 4, 5, 1]
"""

from collections import deque

def solve():
    n, m = map(int, input().split())
    importance = list(map(int, input().split()))
    documents = [(importance[i], i) for i in range(n)]
    q = deque(documents)
    importance.sort()
    cnt = 0
    while True:
        if q[0][0] == importance[-1]:
            cnt += 1
            if q[0][1] == m:
                return cnt
            q.popleft()
            importance.pop()
        else:
            q.rotate(-1)

T = int(input())
for _ in range(T):
    print(solve())


"""
6 0
1 1 9 1 1 1
"""