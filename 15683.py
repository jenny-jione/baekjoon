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