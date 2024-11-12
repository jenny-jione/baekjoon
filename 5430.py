"""
문제 이름: AC
문제 링크: https://www.acmicpc.net/problem/5430
문제 티어: 골드 5

타임라인
2024.11.12 03:02pm~03:51pm (49분)  total: 49분

<정리>
1. 문자열 파싱
2. 덱 
3. 인덱스 다루기
"""

# 통과한 코드
T = int(input())
for _ in range(T):
    cmds = input()
    n = int(input())
    arr = []
    arr_raw = input()[1:-1]
    if arr_raw:
        arr = list(map(int, arr_raw.split(',')))
    
    if len(arr) < cmds.count('D'):
        print('error')
    else:
        head, tail, direct = 0, n-1, 1
        for cmd in cmds:
            if cmd == 'R':
                head, tail = tail, head
                direct *= -1
            else:
                head += direct
        result = [arr[i] for i in range(head, tail+direct, direct)]
        print(f"[{','.join(map(str, result))}]")


# 개선
T = int(input())
for _ in range(T):
    cmds = input()
    n = int(input())
    arr = []
    arr_raw = input()[1:-1]
    arr = arr_raw.split(',') if arr_raw else []

    if len(arr) < cmds.count('D'):
        print('error')
        continue

    head, tail, direct = 0, n-1, 1
    for cmd in cmds:
        if cmd == 'R':
            head, tail = tail, head
            direct *= -1
        else:
            head += direct
    result = [arr[i] for i in range(head, tail+direct, direct)]
    print('['+','.join(result)+']')



# 개선 2 - 덱과 R개수 이용
from collections import deque

T = int(input())
for _ in range(T):
    p = input()
    n = int(input())
    arr = []
    if n > 0:
        arr = input()[1:-1].split(',')
    
    if p.count('D') > len(arr):
        print('error')
        continue

    q = deque(arr)

    rev = 0
    for cmd in p:
        if cmd == 'R':
            rev += 1
        else:
            if rev % 2 == 0:
                q.popleft()
            else:
                q.pop()
    
    if rev % 2 == 1:
        q.reverse()
    
    print('[' + ','.join(q) + ']')