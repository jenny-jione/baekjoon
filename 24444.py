"""
문제 이름: 너비 우선 탐색 1
문제 링크: https://www.acmicpc.net/problem/24444

타임라인
2024.4.10 2:40pm~2:55pm (15분)
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

for i in range(N+1):
    graph[i].sort()

def bfs(graph, start, visited):
    cnt = 1
    q = deque([start])
    while q:
        v = q.popleft()
        for x in graph[v]:
            if visited[x] == 0:
                cnt += 1
                visited[x] = cnt
                q.append(x)

visited = [0] * (N+1)
visited[R] = 1
bfs(graph, R, visited)

for i in range(1, N+1):
    print(visited[i])