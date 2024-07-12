"""
문제 이름: 큐
문제 링크: https://www.acmicpc.net/problem/10845
문제 티어: 실버 4

타임라인
2024.07.12 02:09pm~02:35pm (26분)  total: 26분

<정리>
1. 웬만하면 sys.stdin.readline으로 입력 받자.
2. deque의 popleft와 list의 pop(0)은 같은 역할이다.
"""

# 내 코드 - deque 사용
import sys
input = sys.stdin.readline
from collections import deque
q = deque()
n = int(input().rstrip())
for _ in range(n):
    cmd = input().rstrip().split()
    if cmd[0] == 'push':
        q.append(cmd[1])
    elif cmd[0] == 'pop':
        if q:
            print(q.popleft())
        else:
            print(-1)
    elif cmd[0] == 'size':
        print(len(q))
    elif cmd[0] == 'empty':
        if q:
            print(0)
        else:
            print(1)
    elif cmd[0] == 'front':
        if q:
            x = q.popleft()
            print(x)
            q.appendleft(x)
        else:
            print(-1)
    else:
        if q:
            x = q.pop()
            print(x)
            q.append(x)
        else:
            print(-1)