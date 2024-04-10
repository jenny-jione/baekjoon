"""
문제 이름: DFS와 BFS
문제 링크: https://www.acmicpc.net/problem/1260

타임라인
2024.4.10 3:13pm~3:28pm (15분)
"""

import sys
from collections import deque

input = sys.stdin.readline

N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    if v not in graph[u]:
        graph[u].append(v)
    if u not in graph[v]:
        graph[v].append(u)

for i in range(1, N+1):
    graph[i].sort()

def dfs(graph, v, visited):
    visited[v] = 1
    print(v, end=' ')
    for x in graph[v]:
        if visited[x] == 0:
            dfs(graph, x, visited)
    
def bfs(graph, start, visited):
    visited[start] = 1
    print(start, end=' ')
    q = deque([start])
    while q:
        v = q.popleft()
        for x in graph[v]:
            if visited[x] == 0:
                visited[x] = 1
                print(x, end=' ')
                q.append(x)

check1 = [0] * (N+1)
check2 = [0] * (N+1)
dfs(graph, V, check1)
print()
bfs(graph, V, check2)
