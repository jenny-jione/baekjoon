"""
문제 이름: 숨바꼭질 4
문제 링크: https://www.acmicpc.net/problem/13913
문제 티어: 골드 4

타임라인
2024.08.28 12:49pm~01:27pm (38분)
2024.08.28 03:28pm~03:58pm (30분)  total: 68분

<정리>
1. visited 배열에 방문 정보와 이전 노드 정보를 둘 다 우겨넣으려고 하지 않고 둘을 분리하면 쉽게 풀 수 있다.
2. visited 말고 dist라고 정의한 뒤 -> 걸리는 시간을 기록한다
3. move 배열을 정의한 뒤 -> 이전 노드를 기록한다
"""

# 내가 통과한 코드
from collections import deque

N, K = map(int, input().split())

def solve(n, k):
    visited = [0] * 100001
    path = []
    q = deque([n])
    visited[n] = n
    while q:
        x = q.popleft()
        if x == k:
            while x != n:
                path.append(x)
                prev = visited[x]
                x = prev
            path.append(n)
            break
        for i in (x+1, x-1, x*2):
            if 0<=i<100001 and not visited[i]:
                q.append(i)
                visited[i] = x
    return len(path)-1, path

if N==0 and K==0:
    print(0)
    print(0)
    exit()
elif N==0:
    t, path = solve(1, K)
    path.append(0)
    print(t+1)
    print(*path[::-1])
else:
    t, path = solve(N, K)
    print(t)
    print(*path[::-1])


# visited -> dist, move 로 분리한 코드
from collections import deque

N, K = map(int, input().split())
dist = [0] * 100001
move = [0] * 100001

q = deque([N])
while q:
    x = q.popleft()
    if x == K:
        break
    for i in (x+1, x-1, x*2):
        if 0<=i<=100000 and not dist[i]:
            q.append(i)
            dist[i] = dist[x] + 1
            move[i] = x

print(dist[K])
path = []
x = K
for _ in range(dist[K]+1):
    path.append(x)
    x = move[x]
print(*(path[::-1]))