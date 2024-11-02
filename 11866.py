"""
문제 이름: 요세푸스 문제 0
문제 링크: https://www.acmicpc.net/problem/11866
문제 티어: 실버 4

타임라인
2024.11.01 04:13pm~04:20pm (7분)  total: 7분

<정리>
1. deque
2. f-string, join(), map
"""

from collections import deque
n, k = map(int, input().split())
q = deque([i for i in range(1, n+1)])
result = []
while q:
    q.rotate(-(k-1))
    result.append(q.popleft())
print('<', end='')
print(*result, sep=', ', end='')
print('>')


# 출력 부분 개선 - f-string, join(), map 사용
from collections import deque
n, k = map(int, input().split())
q = deque([i for i in range(1, n+1)])
result = []
while q:
    q.rotate(-(k-1))
    result.append(q.popleft())
print(f"<{', '.join(map(str, result))}>")