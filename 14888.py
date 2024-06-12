"""
문제 이름: 연산자 끼워넣기
문제 링크: https://www.acmicpc.net/problem/14888

타임라인
2024.4.14 00:04am~1:27am (83분)

이 문제에서 사용한 것 or 배운 것
1. dfs -> 백트래킹
2. 나는 사용하지 않았지만 다른 코드를 보니 min, max값 초기 설정할 때 1e9, -1e9로 쓰더라.
"""

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

#   0 1 2 3
#   + - * //
def dfs(ops, li: list):
    global min_val, max_val
    if ops[0]==0 and ops[1]==0 and ops[2]==0 and ops[3]==0:
        val = calculate(numbers, li)
        min_val = min(min_val, val)
        max_val = max(max_val, val)
        return
    for i in range(4):
        if ops[i]>0:
            ops[i] -= 1
            li.append(i)
            dfs(ops, li)
            ops[i] += 1
            li.pop()

def calculate(number, operator):
    result = number[0]
    for i in range(N-1):
        if operator[i]==0:
            result += number[i+1]
        elif operator[i]==1:
            result -= number[i+1]
        elif operator[i]==2:
            result *= number[i+1]
        else:
            if result < 0:
                tmp = result*-1
                tmp //= number[i+1]
                result = tmp * -1
            else:
                result //= number[i+1]
    return result

N = int(input())
numbers = list(map(int, input().split()))
ops = list(map(int, input().split()))
min_val = 1000000001
max_val = -1000000001
dfs(ops, [])

print(max_val)
print(min_val)


####

# 다시 풀기 (통과)
"""
타임라인
2024.06.12 12:16pm~12:40pm (24분)
2024.06.12 12:50pm~12:57pm (7분)  total: 31분

<정리>
1. -10억까지도 중간 결과가 나올 수 있음. 그래서 max_val 초기값은 0이 아니라 -1e9 !
2. 음수를 나눌 때는 조건문 없이 int()로 간단히 해결이 가능하다.
    int(음수/나누는수)로 하면 간단.
    >>> 7 // 2
    3
    >>> 7 / 2
    3.5
    >>> int(7 / 2)
    3
    >>> -7 // 2
    -4
    >>> -7 / 2
    -3.5
    >>> int(-7 / 2)
    -3
"""

N = int(input())
nums = list(map(int, input().split()))
op = list(map(int, input().split()))
max_val = -int(1e9)
min_val = int(1e9)

def dfs(idx, val, op):
    global max_val, min_val
    if idx == N-1:
        max_val = max(max_val, val)
        min_val = min(min_val, val)
        return
    cur = nums[idx+1]
    if op[0] > 0:
        op[0] -= 1
        dfs(idx+1, val+cur, op)
        op[0] += 1
    if op[1] > 0:
        op[1] -= 1
        dfs(idx+1, val-cur, op)
        op[1] += 1
    if op[2] > 0:
        op[2] -= 1
        dfs(idx+1, val*cur, op)
        op[2] += 1
    if op[3] > 0:
        op[3] -= 1
        if val < 0:
            temp = ((-val)//cur)*-1
        else:
            temp = val//cur
        dfs(idx+1, temp, op)
        # 이 한줄로 간결하게 바꾸기 가능.
        # dfs(idx+1, int(val/cur), op)
        op[3] += 1

dfs(0, nums[0], op)
print(max_val)
print(min_val)