"""
문제 이름: 요세푸스 문제
문제 링크: https://www.acmicpc.net/problem/1158
문제 티어: 실버 4

타임라인
2024.07.12 02:44pm~02:54pm (10분)  total: 10분

<정리>
1. deque의 rotate
    1) rotate(양수): 오른쪽으로 회전
    2) rotate(음수): 왼쪽으로 회전
"""

from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().rstrip().split())
q = deque([str(i) for i in range(1, n+1)])
result = []
while q:
    q.rotate(1-k)
    result.append(q.popleft())
print('<'+', '.join(result)+'>')