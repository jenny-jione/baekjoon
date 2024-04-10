"""
문제 이름: 숨바꼭질
문제 링크: https://www.acmicpc.net/problem/1697

타임라인
2024.4.8 1:10pm~3:21pm (131분)
"""

n, k = map(int, input().split())
visited = [0] * 200001
visited[n] = 1
line = [(n, 0)]
pos = n

def move(pos, sec):
    result = []
    new_pos = [pos-1, pos+1, 2*pos]
    for np in new_pos:
        if np < 0:
            continue
        if np > n+k+1:
            continue
        if visited[np] == 0:
            result.append(np)
            visited[np] = 1
    return [result, sec+1]

cur = 0
sec = 0
flag = 0

while(not flag):
    if pos == k:
        print(sec)
        break
    newpos, newsec = move(pos, sec)
    for np in newpos:
        print(np, newsec)
        line.append((np, newsec))
    cur += 1
    pos = line[cur][0]
    sec = line[cur][1]


"""
<두 번째 시도>

타임라인
2024.4.10 3:40pm~4:24pm (44분)
"""

import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())
q = deque([[N]])

def bfs():
    esc = False
    t = 0
    while q:
        if esc:
            break
        li = q.popleft()
        res = []
        for i in li:
            if i == K:
                print(t)
                esc = True
                break
            i1, i2, i3 = i-1, i+1, i*2
            if i1 >= 0 and visited[i1] == 0:
                visited[i1] = 1
                res.append(i1)
            if i2 <= 100000 and visited[i2] == 0:
                visited[i2] = 1
                res.append(i2)
            if i3 <= 100000 and visited[i3] == 0:
                visited[i3] = 1
                res.append(i3)
        q.append(res)
        t += 1

visited = [0] * 200000
bfs()


"""
두번째 코드에 대한 개선점
1. for next_i in (i-1, i+1, i*2): 을 사용해서 코드를 간결하게 바꿨다.
2. esc 변수 대신 리턴을 사용하면 2중 루프 탈출에 대한 고민을 안해도 된다.
    애초에 bfs를 함수로 만들었으니 return을 사용하자.
3. t 변수 대신 visited 값에 시간을 할당한다면
    res도 안써도 되고 q 안에 리스트 대신 각 위치값만 간결하게 저장할 수 있다.
4. python은 조건으로 a < x < b 가 가능하다.
5. MAX 상수를 할당해서 쓰자.
    일일이 100000을 안써도 된다.
"""
import sys
from collections import deque

input = sys.stdin.readline
N, K = map(int, input().split())
MAX = 100001

def bfs():
    q = deque([N])
    while q:
        i = q.popleft()
        if i == K:
            return visited[i]
        for next_i in (i-1, i+1, i*2):
            if 0 <= next_i < MAX and visited[next_i] == 0:
                visited[next_i] = visited[i] + 1
                q.append(next_i)

visited = [0] * MAX
print(bfs())