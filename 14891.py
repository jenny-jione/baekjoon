"""
문제 이름: 톱니바퀴
문제 링크: https://www.acmicpc.net/problem/14891

타임라인
2024.05.23 11:10am~11:50am (40분)
2024.05.23 11:55am~12:15pm (20분)
2024.05.23 1:12pm~1:46pm (34분)

배운 것
1. 지수는 ** 로 간단히 사용한다.
    ex) 2의 3제곱은 2**3

공부할 것
1. deque의 rotate
"""


import sys
input = sys.stdin.readline

ORDER = {
    1: [(1, 2), (2, 3), (3, 4)],
    2: [(2, 1), (2, 3), (3, 4)],
    3: [(3, 2), (3, 4), (2, 1)],
    4: [(4, 3), (3, 2), (2, 1)]
}

gear_rotate = [0]*5

gear = [0]
for _ in range(4):
    gear.append(list(map(int, input().strip())))

k = int(input())
cmd = []
for _ in range(k):
    gn, dir = map(int, input().split())
    cmd.append((gn, dir))

# gear1이 d 방향으로 회전할 때 gear2의 회전 방향을 결정
def calculate_dir(g1, g2, r):
    gear1, gear2 = gear[g1], gear[g2]
    if r==0:
        return 0
    # g2 g1 순서일 경우 g2[2]==g1[6]를 비교
    if g2 < g1:
        if gear2[2]==gear1[6]:
            return 0
        else:
            return r*-1
    # g1 g2 순서일 경우 g1[2]==g2[6]를 비교
    if g1 < g2:
        if gear1[2]==gear2[6]:
            return 0
        else:
            return r*-1

# 1:cw, -1:ccw, 0:stop
def rotate(gr: list, cw: int):
    result = [0]*8
    if cw==0:
        return gr
    if cw==1:
        for i in range(8):
            result[(i+1)%8] = gr[i]
    elif cw==-1:
        for i in range(8):
            result[i-1] = gr[i]
    return result

for gn, dir in cmd:
    gear_rotate[gn] = dir
    for g1, g2 in ORDER[gn]:
        gear_rotate[g2] = calculate_dir(g1, g2, gear_rotate[g1])

    for i in range(1, 4+1):
        gear[i] = rotate(gear[i], gear_rotate[i])

answer = 0
for i in range(1, 5):
    answer += gear[i][0] * (2**(i-1))
print(answer)