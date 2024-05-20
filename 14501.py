"""
문제 이름: 퇴사
문제 링크: https://www.acmicpc.net/problem/14501

타임라인
2024.4.8 11:38pm
~ 2024.4.9 7:45pm
계속 붙잡고 있느라 .. 3시간 붙잡고 있다가 결국 답 코드 봄
"""

n = int(input())
cs = []
for _ in range(n):
    t, p = map(int, input().split())
    cs.append((t, p))

# 내가 원하던 풀이 .. !
def consult(i, rev):
    global max_rev
    if i == n:
        max_rev = max(max_rev, rev)
        return
    # i일에 상담 안하는 경우 전날과 rev는 같음. 상담 안해서 idx일에 수입 0이므로.
    consult(i+1, rev)
    # 상담 가능한 경우 다음 날짜는 i + t
    if i + cs[i][0] <= n:
        consult(i+cs[i][0], rev+cs[i][1])

max_rev = 0
consult(0, 0)
print(max_rev)


"""
다시풀기2

타임라인
2024.05.02 4:13pm~4:23pm (10분)
2024.05.02 4:35pm~5:00pm (25분)
2024.05.02 5:02pm~5:12pm (10분)
2024.05.03 11:01am~11:51am (50분)
--- 코드 참고 ---
2024.05.03 11:51am~12:04am (13분)
"""


# 틀린 코드
def solve(day, rev, sched):
    global max_rev
    print(f'sced:{sched}, day:{day}')
    if day>N or day+cs[day][0]>N+1:
        max_rev = max(max_rev, rev)
        print('schedule:', sched, rev)
        return
    print('잉')
    """
    반례:
3
5 10
2 10
1 10
solve를 맨 처음 호출했을 때부터 종료조건에 걸려버려서
재귀함수 호출도 하기 전에 그냥 return 되어버림..;;
그니까 이 아래 코드가 한 번도 실행되지 않고 끝나는 것..
    """
    solve(day+cs[day][0], rev+cs[day][1], sched+[day])
    print('여기는 옴?')
    solve(day+1, rev, sched)

solve(1, 0, [])
print(max_rev)


# 코드 참고 후 다시 짠 코드
N = int(input())

cs = [(0, 0)]
for _ in range(N):
    t, p = map(int, input().strip().split())
    cs.append((t, p))

max_rev = 0

def solve(day, rev):
    global max_rev
    if day>N:
        max_rev = max(max_rev, rev)
        return
    
    solve(day+1, rev)

    if day+cs[day][0] <= N+1:
        solve(day+cs[day][0], rev+cs[day][1])

solve(1, 0)
print(max_rev)



"""
다시풀기3

타임라인
2024.05.20 3:15pm~3:30pm (15분)

코드 안보고 한 번에 성공!

* 이전 코드와 다르게 짠 부분
1. cs 리스트 안에 tuple이 아니라 list로 넣음
    전) t, p = map(int, input().strip().split())
        cs.append((t, p))

    후) cs.append(list(map(int, input().split())))
"""

import sys
input = sys.stdin.readline

N = int(input())
cs = [[0, 0]]
for _ in range(N):
    cs.append(list(map(int, input().split())))

max_rev = 0
def solve(day, rev):
    global max_rev
    if day > N:
        max_rev = max(max_rev, rev)
        return
    
    solve(day+1, rev)
    if day+cs[day][0] <= N+1:
        solve(day+cs[day][0], rev+cs[day][1])

solve(1, 0)
print(max_rev)


"""
3
5 10
6 20
1 100
"""