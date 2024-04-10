"""
문제 이름: 너비 우선 탐색 2
문제 링크: https://www.acmicpc.net/problem/24445

타임라인
2024.4.10 3:01pm~3:09pm (8분)
"""

import sys
from collections import deque
input = sys.stdin.readline

N, M, R = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, N+1):
    graph[i].sort(reverse=True)


def bfs(graph, start, visited):
    q = deque([start])
    cnt = 1
    while q:
        u = q.popleft()
        for v in graph[u]:
            if visited[v] == 0:
                cnt += 1
                visited[v] = cnt
                q.append(v)

visited = [0] * (N+1)
visited[R] = 1
bfs(graph, R, visited)

for i in range(1, N+1):
    print(visited[i])


# deque를 쓰는 이유? collections에서?? popleft 때문에?