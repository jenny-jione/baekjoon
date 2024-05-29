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



#
"""
rotate를 이용하여 다시 풀기! => 통과!
2024.05.29 04:22pm~05:00pm (38분)
2024.05.29 05:40pm~05:47pm (7분)

코드 짜고 예제 입력으로 테스트하는데 3, 4가 실패.
이유를 찾아보니 gear_direction을 매 cmd마다 초기화해야 하는데 하나로 사용해서 틀린거였다!
for문 안에서 새로 초기화를 해주었더니 통과!

1. 파이썬에서는 함수 내부에서 전역 변수에 직접 접근하고 수정할 수 있다.
    그래서 check와 gear_direction을 함수 밖에서 초기화한 뒤,
    make_direction과 rotate_gears 함수 내에서 변수를 참조할 때,
    해당 변수가 함수 내부에 선언되어 있지 않다면,
    파이썬은 변수의 값을 찾기 위해 함수 외부의 범위(즉, 전역 범위)로 이동한다.

2. 리스트 변수를 초기화할 때, [0, 0, 0, 0, 0] 대신 간결하게 [0]*5를 사용하자.
"""
from collections import deque

gears = [0]
for _ in range(4):
    gears.append(deque(list(map(int, input().strip()))))
K = int(input())
cmd = []
for _ in range(K):
    cmd.append(list(map(int, input().split())))

def make_direction(gn, direct):
    # 현재 기어의 회전 방향 할당
    gear_direction[gn] = direct
    check[gn] = 1
    if direct==0:
        return
    if gn>1:
        # 왼쪽 기어 정해주기
        if check[gn-1]==0:
            if gears[gn-1][2] == gears[gn][6]:
                make_direction(gn-1, 0)
            else:
                make_direction(gn-1, direct*(-1))
    if gn<4:
        if check[gn+1]==0:
            # 오른쪽 기어 정해주기
            if gears[gn][2] == gears[gn+1][6]:
                make_direction(gn+1, 0)
            else:
                make_direction(gn+1, direct*(-1))
    return

def rotate_gears():
    for i in range(1, 5):
        gears[i].rotate(gear_direction[i])

for gn, d in cmd:
    # check = [0, 0, 0, 0, 0]
    # gear_direction = [0, 0, 0, 0, 0]
    check = [0]*5
    gear_direction = [0]*5
    make_direction(gn, d)
    rotate_gears()

# 점수 계산
answer = 0
for i in range(4):
    answer += gears[i+1][0] * (2**i)
print(answer)