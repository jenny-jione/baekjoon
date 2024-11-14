"""
문제 이름: 케빈 베이컨의 6단계 법칙
문제 링크: https://www.acmicpc.net/problem/1389
문제 티어: 실버 1

타임라인
2024.11.14 01:33pm~02:08pm (35분)  total: 35분

<정리>
1. bfs
2. 설정한 변수를 잘 살피기 .. 
    N, M 받아두고 for의 range범위를 잘못 설정해서 인덱스 에러남
"""

from collections import deque

def bfs(start, graph):
    q = deque([start])
    visited = [-1] * (N+1)
    visited[start] = 0
    while q:
        x = q.popleft()
        for nx in graph[x]:
            if visited[nx] == -1:
                q.append(nx)
                visited[nx] = visited[x] + 1
    return sum(visited[1:])

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    if a not in graph[b]:
        graph[b].append(a)
    if b not in graph[a]:
        graph[a].append(b)

kb, answer = int(1e9), 0
for i in range(1, N+1):
    cnt = bfs(i, graph)
    if cnt < kb:
        answer = i
        kb = cnt
print(answer)