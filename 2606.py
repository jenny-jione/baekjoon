"""
문제 이름: 바이러스
문제 링크: https://www.acmicpc.net/problem/2606

타임라인
2024.4.9 2:15pm~2:23pm (8분)
"""

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(graph, v, visited):
    global cnt
    cnt += 1
    visited[v] = 1
    for x in graph[v]:
        if visited[x] == 0:
            dfs(graph, x, visited)

visited = [0] * (N+1)
cnt = 0
dfs(graph, 1, visited)
if cnt == 0:
    print(cnt)
else:
    print(cnt-1)