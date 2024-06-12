"""
문제 이름: 컨베이어 벨트 위의 로봇
문제 링크: https://www.acmicpc.net/problem/20055
문제 티어: 골드 5

타임라인
2024.06.12 03:29pm~04:01pm (32분)
2024.06.12 04:10pm~04:23pm (13분)  total: 45분

<정리>
1. deque 복습
2. reversed 복습 (역순 range는 아직도 헷갈린다) 
3. 구현 문제는 모 든 조 건 을 꼼 꼼 히 보 고 정 확 히 구 현 해 야 한 다 !
4. 이 코드는 python으로는 시간초과, pypy3으로는 통과함.
"""

from collections import deque

N, K = map(int, input().split())
q = deque(list(map(int, input().split())))
robot = [0] * N

step = 0
while True:
    step += 1
    # 1.벨트와 로봇이 회전
    q.rotate(1)
    for i in reversed(range(N-1)):
        robot[i+1] = robot[i]
    robot[N-1] = 0
    robot[0] = 0

    # 2.로봇이 한칸씩 이동
    robot[N-1] = 0
    for i in reversed(range(N-1)):
        if robot[i]==1 and robot[i+1]==0 and q[i+1]>=1:
            robot[i+1] = robot[i]
            robot[i] = 0
            q[i+1] -= 1
    
    # 3.올리는 위치에 로봇 올리기
    if q[0] != 0:
        robot[0] = 1
        q[0] -= 1

    # 4.내구도 확인 후 과정 종료 여부
    zero = 0
    for i in range(N*2):
        if q[i] == 0:
            zero += 1
    if zero >= K:
        break

print(step)