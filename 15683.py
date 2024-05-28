"""
문제 이름: 감시
문제 링크: https://www.acmicpc.net/problem/15683

타임라인
2024.5.24 10:21am~10:36am (15분)
2024.5.24 12:55pm~1:25pm (30분)
2024.5.24 2:33pm~2:54pm (21분)
-- 구글링해서 코드 참고 --
2024.5.25 8:55pm~9:38pm (43분)

<이 문제에서 배운 것>
1. 최소값 구할 때 초기값 설정을 int(1e9)로 한다.
2. dy, dx를 잘 쓰자.
3. dfs는 아직도 연습이 필요하다.
4. 벽이나 사무실 끝에 닿을 때까지 감시 영역을 칠하는 것을 하나의 함수로 할 수 있다.
    이 때 dy, dx를 활용한다
5. 각 cctv마다 감시 방법이 나누어지는데 이것도 dy, dx를 이용해서 하나의 변수로 표현할 수 있다.
"""

import copy

N, M = map(int, input().strip().split())
office = []
cctvs = []

mode = [
    [],
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3]],
    [[0, 1], [1, 2], [2, 3], [3, 0]],
    [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
    [[0, 1, 2, 3]]
]

dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]

for i in range(N):
    data = list(map(int, input().split()))
    office.append(data)
    for j in range(M):
        if data[j] in range(1, 6):
            cctvs.append([data[j], i, j])

def fill(temp_office, direction, y, x):
    for i in direction:
        ny, nx = y, x
        while True:
            ny += dy[i]
            nx += dx[i]
            if ny < 0 or ny >= N or nx < 0 or nx >= M:
                break
            if temp_office[ny][nx] == 6:
                break
            elif temp_office[ny][nx] == 0:
                temp_office[ny][nx] = -1

def dfs(depth, office):
    global min_val
    if depth==len(cctvs):
        cnt = 0
        for i in range(N):
            cnt += office[i].count(0)
        min_val = min(min_val, cnt)
        return
    temp = copy.deepcopy(office)
    cctv_num, y, x = cctvs[depth]
    for direction in mode[cctv_num]:
        fill(temp, direction, y, x)
        dfs(depth+1, temp)
        temp = copy.deepcopy(office)

min_val = int(1e9)
dfs(0, office)
print(min_val)


#
"""
다시풀기

타임라인
2024.5.28 1:51pm~1:57pm (6분)
2024.5.28 2:09pm~2:46pm (27분)
2024.5.28 2:51pm~3:15pm (24분)
2024.5.28 3:22pm~3:32pm (10분)
통과!

느낀점 & 배운것
1. cctv_num, y, x = cctv_set[depth] 한 줄로 변수 3개를 한 번에 할당할 수 있다.
    이번에 내가 한 방법
        cctv_num = cctv_set[depth][0]
        함수 호출할 때 y, x 대신 cctv_set[depth][1], cctv_set[depth][2]로 번거롭게 접근함
2. dfs를 사용할 때는 '이게 첫 번째 호출인가?' 같은 생각은 하지 말자.
    재귀함수이기 때문에 이게 몇 번째 호출이든 상관없이 적용되는 코드를 짜야 함.
"""

import copy
N, M = map(int, input().split())

cctv = [
    [],
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3]],
    [[0, 1], [1, 2], [2, 3], [3, 0]],
    [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
    [[0, 1, 2, 3]]
]

dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]

office = []
cctv_set = []
for y in range(N):
    data = list(map(int, input().strip().split()))
    office.append(data)
    for x in range(M):
        if data[x] in [1, 2, 3, 4, 5]:
            cctv_set.append([data[x], y, x])

def monitor(mode, office, y, x):
    for direct in mode:
        ny, nx = y, x
        while True:
            ny += dy[direct]
            nx += dx[direct]
            if ny not in range(N) or nx not in range(M) or office[ny][nx]==6:
                break
            office[ny][nx] = -1

def dfs(depth, office):
    global min_val
    if depth==len(cctv_set):
        unseen = 0
        for i in range(N):
            unseen += office[i].count(0)
        min_val = min(min_val, unseen)
        return min_val
    cctv_num = cctv_set[depth][0]
    temp_office = copy.deepcopy(office)
    for mode in cctv[cctv_num]:
        monitor(mode, temp_office, cctv_set[depth][1], cctv_set[depth][2])
        dfs(depth+1, temp_office)
        temp_office = copy.deepcopy(office)

min_val = 65
dfs(0, office)
print(min_val)