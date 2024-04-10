"""
문제 이름: 깊이 우선 탐색 2
문제 링크: https://www.acmicpc.net/problem/24480

타임라인
2024.4.10 1:49pm~2:02pm (13분)
"""

import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N, M, R = map(int, input().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, N+1):
    graph[i].sort(reverse=True)

visited = [0] * (N+1)
cnt = 0
def dfs(graph, r, visited):
    global cnt
    cnt += 1
    visited[r] = cnt
    for x in graph[r]:
        if visited[x] == 0:
            dfs(graph, x, visited)

dfs(graph, R, visited)
for i in range(1, N+1):
    print(visited[i])