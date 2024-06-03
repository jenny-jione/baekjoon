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



# 다시 풀기 (5.31)
"""
다시풀기

2024.05.31 01:18pm~01:50pm (32분)
2024.05.31 02:07pm~02:39pm (32분)
2024.05.31 03:17pm~03:57pm (40분)
--- 시간초과 나서 힌트 봄 .. 처음 풀 때랑 똑 같 이 접근하고 있었네..ㅎ
내 접근법: closed circle 찾기
힌트: 인접한 정점은 다른 색으로 칠해야 한다

질문
1. K만큼 반복문 하는데.. 그 안에 다 구현하는게 맞나? 뭔가 함수로 따로 빼야 하지 않을까?
"""
# 시간초과 코드
# import sys
# input = sys.stdin.readline

# def dfs(graph, start, v, circle: list):
#     global closed
#     for u in graph[v]:
#         if v!=start and u==start and len(circle)>=3:
#             if len(circle)%2==1:
#                 closed = True
#                 return
#     for u in graph[v]:
#         if not visited[u]:
#             visited[u] = 1
#             circle.append(u)
#             dfs(graph, start, u, circle)
#             visited[u] = 0
#             circle.pop()

# K = int(input())
# for _ in range(K):
#     V, E = map(int, input().split())
#     graph = [[] for _ in range(V+1)]
#     for _ in range(E):
#         u, v = map(int, input().split())
#         graph[u].append(v)
#         graph[v].append(u)
#     visited = [0]*(V+1)
#     for i in range(1, V+1):
#         closed = False
#         visited[i] = 1
#         dfs(graph, i, i, [i])
#         visited[i] = 0
#         if closed:
#             print('NO')
#             break
#     else:
#         print('YES')


# 힌트+코드 참고.. 이번엔 dfs로.
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline  # 이거 안하니까 시간초과남. 이 한 줄 추가하고 바로 통과함
K = int(input())

def paint(v, color):
    visited[v] = color

    for u in graph[v]:
        if not visited[u]:
            result = paint(u, -color)
            if not result:
                return False
        else:
            if visited[u]==color:
                return False
    return True

for _ in range(K):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    for _ in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    visited = [0]*(V+1)
    
    for i in range(1, V+1):
        if not visited[i]:
            result = paint(i, 1)
            if not result:
                break
    if result:
        print('YES')
    else:
        print('NO')