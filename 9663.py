"""
문제 이름: N-Queen
문제 링크: https://www.acmicpc.net/problem/9663
문제 티어: 골드 4

타임라인
2024.06.10~2024.6.11

<정리>
1. abs()는 시간초과남.
2. 대각선 관계인지를 수식으로 표현하자. 그러면 단순히 덧셈뺄셈이므로 연산비용이 줄어든다. 그래서 통과함.
    1) 우하향(좌상향)의 대각선끼리는 y와 x 좌표의 차가 같다.
        y와 x 모두 r만큼 전진하거나 후진하므로, 
        (y+r, x+r) 이거나 (y-r, x-r) 이므로, 뺄셈을 하면 y-x만 남음.
    2) 우상향(좌하향)의 대각선끼리는 y와 x 좌표의 합이 같다.
        y가 r만큼 전진하면 x는 r만큼 후진하므로
        (y+r, x-r) 이거나 (y-r, x+r) 이므로, 덧셈을 하면 y+x만 남음.
3. 백트래킹. 유망한지를 확인하고 append, 재귀, pop.
4. pypy로 제출해야됨..
"""

# 내 코드 - 시간초과
n = int(input())
cnt = 0

def not_attack(y, x, qli):
    for y0, x0 in qli:
        if x == x0:
            return False
        if (y-y0)==abs(x-x0):
            return False
    return True

def choose_queen(y, qli: list):
    global cnt
    if len(qli)==n:
        cnt += 1
        return
    for x in range(n):
        if not_attack(y, x, qli):
            qli.append((y, x))
            choose_queen(y+1, qli)
            qli.pop()

choose_queen(0, [])
print(cnt)


# 남의 코드
def attack(y, x):
    for i in range(y):
        if arr[i]==x or y+x==arr[i]+i or y-x==i-arr[i]:
            return True
    return False

def func(y):
    global cnt
    if y == n:
        cnt += 1
        return

    for x in range(n):
        if not attack(y, x):
            arr.append(x)
            func(y+1)
            arr.pop()

n=int(input())

cnt=0
arr=[]
func(0)
print(cnt)


## 다시 풀기
def attack(y, x):
    for i in range(y):
        # if arr[i] == x or abs(y-i)==abs(x-arr[i]): # 시간초과.
        if arr[i] == x or y+x==arr[i]+i or y-x==i-arr[i]: # 통과
            return True
    return False

def place_queen(y):
    global cnt
    if y==n:
        cnt += 1
        return
    for x in range(n):
        if not attack(y, x):
            arr.append(x)
            place_queen(y+1)
            arr.pop()

cnt = 0
arr = []
n = int(input())
place_queen(0)
print(cnt)