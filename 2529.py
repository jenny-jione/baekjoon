"""
문제 이름: 부등호
문제 링크: https://www.acmicpc.net/problem/2529
문제 티어: 실버 1

타임라인
2024.08.13 01:18pm~01:50pm (32분)  total: 32분

<정리>
"""

# 내 통과 코드
k = int(input())
s = list(input().split())
flag1, flag2 = False, False
visited1 = [0] * 10
visited2 = [0] * 10
max_answer, min_answer = '', ''

def solve_max(idx, cur, res: list):
    global flag1, max_answer
    if flag1 == True:
        return
    if len(res) == k+1:
        flag1 = True
        max_answer = ''.join(map(str, res))
        return
    nxt_sign = s[idx]
    for i in range(9, -1, -1):
        if flag1:
            break
        if not visited1[i]:
            if (nxt_sign == '>' and cur > i) or (nxt_sign=='<' and cur < i):
                visited1[i] = 1
                res.append(i)
                solve_max(idx+1, i, res)
                visited1[i] = 0
                res.pop()

def solve_min(idx, cur, res: list):
    global flag2, min_answer
    if flag2 == True:
        return
    if len(res) == k+1:
        flag2 = True
        min_answer = ''.join(map(str, res))
        return
    nxt_sign = s[idx]
    for i in range(10):
        if flag2:
            break
        if not visited2[i]:
            if (nxt_sign == '>' and cur > i) or (nxt_sign=='<' and cur < i):
                visited2[i] = 1
                res.append(i)
                solve_min(idx+1, i, res)
                visited2[i] = 0
                res.pop()

for i in range(9, -1, -1):
    if flag1:
        break
    if not visited1[i]:
        visited1[i] = 1
        solve_max(0, i, [i])
        visited1[i] = 0

for i in range(10):
    if flag2:
        break
    if not visited2[i]:
        visited2[i] = 1
        solve_min(0, i, [i])
        visited2[i] = 0

print(max_answer)
print(min_answer)



# 간결하게 바꿈 - 근데 시간은 더 걸림
k = int(input())
signs = list(input().split())
visited = [0] * 10
answer = []

def check(cur, nxt, sign):
    if sign == '<':
        return cur < nxt
    else:
        return cur > nxt

def solve(idx, res):
    if idx > k:
        answer.append(res)
        return
    for i in range(10):
        if not visited[i]:
            if idx==0 or check(int(res[-1]), i, signs[idx-1]):
                visited[i] = 1
                solve(idx+1, res+str(i))
                visited[i] = 0
    
solve(0, "")

print(answer[-1])
print(answer[0])