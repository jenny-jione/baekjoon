"""
문제 이름: 뱀과 사다리 게임
문제 링크: https://www.acmicpc.net/problem/16928

타임라인
2024.4.12 10:50am~12:28pm (98분)
2024.4.12 12:45pm~12:56pm (11분)    total: 109분

아이디어:
1. 포탈로 이동했건 주사위를 굴려서 이동했건 한 번 지나간 위치는 다시 지나가지 않는다. 최솟값이니까.
    => portal 배열을 만들어서 주사위를 굴릴 때마다 nx와 portal[nx]를 모두 검사한다.
"""

import sys
from collections import deque
input = sys.stdin.readline

N, M = list(map(int, input().split()))
graph = [0] * 101
portal = [i for i in range(101)]
visited = [0] * 101
for _ in range(N+M):
    start, end = list(map(int, input().split()))
    graph[start] = end
    portal[start] = end

dice = [1, 2, 3, 4, 5, 6]
q = deque([1])
while q:
    x = q.popleft()
    # print(f'pop x({x}) ... {q}')
    # print('portal:', [(s, e) for s, e in enumerate(graph) if e])
    # print('visited:', [(i, v) for i, v in enumerate(visited) if v])
    if x == 100:
        print(visited[x])
        # print('끝!!', x, visited[x])
        break
    for i in range(1, 7):
        # print(f'{x} roll -- {i}')
        nx = x+i
        if nx <= 100 and not visited[nx]:
        # if nx <= 100:
            roll = visited[x] + 1
            visited[nx] = roll
            # portal이 없을 때
            if nx == portal[nx]:
                q.append(nx)
                # print(f'{x}+{i}->{nx} append   {visited[x]}->{visited[portal[nx]]}')
            # portal이 있을 때
            if nx != portal[nx]:
                pnx = portal[nx]
                if not visited[pnx]:
                    visited[pnx] = roll
                    q.append(pnx)
                    # print(f'{x}+{i}({nx})->@@->{pnx} append  {visited[x]}->{visited[pnx]}')
                # else:
                    # print(f'already visit: {pnx}')
    # print()