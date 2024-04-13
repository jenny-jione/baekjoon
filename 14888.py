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