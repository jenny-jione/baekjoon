"""
문제 이름: 깊이 우선 탐색 1
문제 링크: https://www.acmicpc.net/problem/24479

타임라인
2024.4.10 12:03pm~1:20pm (77분)
"""
import sys
sys.setrecursionlimit(10 ** 6)  # 이 코드를 추가해야 런타임에러(Recursion Error)가 나지 않음
input = sys.stdin.readline      # 이 코드를 추가해야 시간초과가 나지 않음

N, M, R = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, N+1):
    graph[i].sort()

def dfs(graph, r, visited):
    global cnt
    cnt += 1
    visited[r] = cnt
    for x in graph[r]:
        if visited[x] == 0:
            dfs(graph, x, visited)

cnt = 0
visited = [0] * (N+1)
dfs(graph, R, visited)

for i in range(1, N+1):
    print(visited[i])



"""
아래는 내 코드인데 메모리 초과가 남.
아마도 graph를 N * N 으로 해서 필요없는 데이터까지 다 저장해둬서 그런 것 같다.
그냥 양방향 간선이기 때문에 u,v가 이어진 것만 저장해야 하는게 아닐까 가 나의 추정.
그래서 아래 말고 위 코드 처럼 해야 하는듯. 
"""
N, M, R = map(int, input().split())
graph = [[0] * (N+1) for _ in range(N+1)]

for _ in range(N):
    u, v = map(int, input().split())
    graph[u][v] = 1
    graph[v][u] = 1

def dfs(adj, r):
    global cnt
    cnt += 1
    order[r] = cnt
    visited[r] = 1
    for i, x in enumerate(adj):
        if x == 1 and visited[i] == 0:
            dfs(graph[i], i)
    return

cnt = 0
visited = [0] * (N+1)
order = [0] * (N+1)
dfs(graph[R], R)

for i in range(1, N+1):
    print(order[i])