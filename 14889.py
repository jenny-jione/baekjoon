"""
문제 이름: 스타트와 링크
문제 링크: https://www.acmicpc.net/problem/14889
문제 티어: 실버 1

타임라인
2024.06.12 11:01am~11:38am (37분)  total: 37분

<정리>
1. 최솟값 구할 때. 초기값 설정을 int(1e9) (10억) 으로 한다.
2. 조합은 (1,7)과 (7,1)이 같은 것이기 때문에 for문의 시작이 1부터가 아니다.
    7부터 탐색할 경우 7보다 작은 숫자는 볼 필요가 없음.
    그래서 재귀함수 호출할 때 start 파라미터가 필요함.
    + 반면 순열의 경우 (1,7)과 (7,1)이 다르기 때문에 항상 처음부터 탐색한다.
"""

# 내 코드 (통과)
N = int(input())
s = []
for _ in range(N):
    s.append(list(map(int, input().split())))

diff_min = int(1e9)
pick = [0] * N
t1, t2 = [], []

def cal_power(team):
    result = 0
    for i in team:
        for j in team:
            if i==j:
                continue
            result += s[i][j]
    return result

def team_pick(cnt, start):
    global t1, t2, diff_min
    if cnt == N//2:
        for i in range(N):
            if pick[i]==1:
                t1.append(i)
            else:
                t2.append(i)
        t1_power, t2_power = cal_power(t1), cal_power(t2)
        diff = abs(t1_power-t2_power)
        diff_min = min(diff_min, diff)
        t1, t2 = [], []
        return
    for i in range(start, N):
        if pick[i] == 0:
            pick[i] = 1
            team_pick(cnt+1, i)
            pick[i] = 0

team_pick(0, 0)
print(diff_min)



####

# 개선한 코드
"""
pick을 계속 활용해서 불필요한 변수 및 함수 선언을 줄였다.
팀 능력치를 구하기 위해서 팀1, 팀2 리스트를 새로 선언할 필요 없이
pick의 값이 둘 다 1이면 t1에 더하고,
pick의 값이 둘 다 0이면 t2에 더하면 된다.
애초애 내가 구현한 pick 리스트가 그 의미임.
 pick[i]==1이면 뽑았다(t1팀에)
 pick[i]==0이면 안뽑았다(t1팀에. 그래서 t2팀 선수임)
+ 근데 코드를 줄였는데 시간은 내 코드보다 더 많이 걸림ㅋㅋㅋ 이유가 뭐지..
"""
import sys
input = sys.stdin.readline
N = int(input().strip())
s = []
for _ in range(N):
    s.append(list(map(int, input().strip().split())))

diff_min = int(1e9)
pick = [0] * N

def solve(cnt, start):
    global diff_min
    if cnt == N//2:
        t1, t2 = 0, 0
        for i in range(N):
            for j in range(N):
                if pick[i] and pick[j]:
                    t1 += s[i][j]
                elif not pick[i] and not pick[j]:
                    t2 += s[i][j]
        diff_min = min(diff_min, abs(t1-t2))
        return
    for i in range(start, N):
        if not pick[i]:
            pick[i] = 1
            solve(cnt+1, i)
            pick[i] = 0

solve(0, 0)
print(diff_min)