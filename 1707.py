"""
문제 이름: 이분 그래프
문제 링크: https://www.acmicpc.net/problem/1707

타임라인
2024.4.12 1:09pm~1:30pm (21분)
2024.4.12 2:54pm~3:54pm (60분)
2024.4.12 5:16pm~5:56pm (40분)
2024.4.12 6:43pm~7:16pm (33분)
2024.4.12 7:30pm~7:40pm (10분)
2024.4.12 10:46pm~11:22pm (36분)
-- 결국 힌트 봄 (인접한 정점은 다른 색으로 칠한다) 코드는 안봄 --
2024.4.12 11:25pm
 ~2024.4.13 12:03am (38분)  total: 238분
"""


import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    visited = [0]*(V+1)
    for _ in range(E):
        u, v = list(map(int, input().split()))
        graph[u].append(v)
        graph[v].append(u)
    for i in range(1, V+1):
        graph[i].sort()
    
    result = 'YES'
    for start in range(1, V+1):
        if not visited[start]:
            visited[start] = 1
            q = deque([start])
            color = 1
            while q:
                v = q.popleft()
                if visited[v] == 1:
                    color = 2
                else:
                    color = 1
                for i in graph[v]:
                    if not visited[i]:
                        visited[i] = color
                        q.append(i)
                    else:
                        if visited[i] == visited[v]:
                            result = 'NO'
                            break
    print(result)
        

    # result = bfs(graph, 1, visited)
    # print(result)
    
    


# [try 4] ... 도저히 모르갯다
# T = int(input())
# for _ in range(T):
#     V, E = map(int, input().split())
#     graph = [[0]*(V+1) for _ in range(V+1)]
#     for _ in range(E):
#         u, v = list(map(int, input().split()))
#         graph[u][v] = 1
#         graph[v][u] = 1
#     print(graph)


# [try 3] bfs - 틀림
# def bfs(graph, start, visited):
#     print()
#     cnt = 0
#     print(f'call bfs :: {start}')
#     q = deque([start])
#     while q:
#         v = q.popleft()
#         print(v)
#         cnt += 1
#         for i in graph[v]:
#             print(f'{i} in {graph[v]}')
#             if not visited[i]:
#                 visited[i] = visited[v] + 1
#                 print(f'{v}->{i}, ({visited[v]}, {visited[i]})')
#                 q.append(i)
#     print(visited)

# T = int(input())
# for _ in range(T):
#     V, E = map(int, input().split())
#     graph = [[] for _ in range(V+1)]
#     for _ in range(E):
#         u, v = map(int, input().split())
#         graph[u].append(v)
#         graph[v].append(u)
    
#     for i in range(1, V+1):
#         graph[i].sort()
    
#     for i in range(1, V+1):
#         visited = [0] * (V+1)
#         bfs(graph, i, visited)



# # [try 2] 틀림 - dfs
# def dfs(graph, v, visited, depth):
#     print(f'dfs call :: {v} visit \t{visited[1:]}-----------{depth}')
#     visited[v] = 1
#     end = 0
#     if v == end:
#         return True
#     for i in graph[v]:
#         print(f'for {i} in {graph[v]}\t\t{visited[1:]}')
#         if not visited[i]:
#             # visited[i] = 1
#             dfs(graph, i, visited, depth+1)
#     return False


# T = int(input())
# for _ in range(T):
#     V, E = map(int, input().split())
#     graph = [[] for _ in range(V+1)]
#     for _ in range(E):
#         u, v = map(int, input().split())
#         graph[u].append(v)
#         graph[v].append(u)
    
#     for i in range(1, V+1):
#         graph[i].sort()
    
#     print(f'==graph : {graph}==')
    
#     # 로직 시작
#     print()
#     # visited = [[0]*(V+1) for _ in range(V+1)]
#     # visited = [0] * (V+1)
#     for i in range(1, V+1):
#         visited = [0] * (V+1)
#         print(f'{i} closed checking start ...')
#         res = dfs(graph, i, visited, 0)
#         print(res)
#         print()


# [try 1] 틀림
# 내가 생각한 논리. edges 중 하나의 (p, q)에 대해서, (q, x)와 (y, p)가 동시에 존재하면 닫힌 그래프. 단 x!=p, y!=q
# T = int(input())
# for _ in range(T):
#     V, E = map(int, input().split())
#     edges = []
#     for _ in range(E):
#         u, v = map(int, input().split())
#         edges.extend([(u, v), (v, u)])
#     closed = False
#     for p, q in edges:
#         closed1, closed2 = False, False
#         for qq, x in edges:
#             if qq==q and x!=p:
#                 closed1 = True
#                 break
#         for y, pp in edges:
#             if y!=q and pp==p:
#                 closed2 = True
#                 break
#         if closed1 and closed2:
#             closed = True
#             break
#     if closed:
#         print('NO')
#     else:
#         print('YES')