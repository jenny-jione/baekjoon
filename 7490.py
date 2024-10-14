"""
문제 이름: 0 만들기
문제 링크: https://www.acmicpc.net/problem/7490
문제 티어: 골드 5

타임라인
2024.10.14 04:09pm~04:30pm (21분)
2024.10.14 09:29pm~10:12pm (43분)  total: 64분

<정리>
1. eval 함수로 코드 간결화 가능.
    eval(문자열) = 식 그대로를 계산해줌.
    ex. print(eval('1+2')) ==> '3'
"""

# 내 코드 (eval 함수 x) --> 64ms
def make_expression(s):
    s = s.replace(' ', '').split('-')
    s2 = []
    for i in s:
        s2.append(i)
        s2.append('-')
    s2.pop()
    result = []
    for i in s2:
        splited = i.split('+')
        if len(splited) >= 2:
            for j in splited:
                result.append(j)
                result.append('+')
            result.pop()
        else:
            result.append(i)
    return result

def calc(exp):
    result = int(exp[0])
    for i in range(1, len(exp)):
        if exp[i] == '+':
            result += int(exp[i+1])
        elif exp[i] == '-':
            result -= int(exp[i+1])
    return result

def solve(nums, i, res):
    global result
    if i == nums[-1]:
        exp_list = make_expression(res)
        if calc(exp_list)==0:
            result.append(res)
        return
    solve(nums, i+1, res+'+'+str(i+1))
    solve(nums, i+1, res+'-'+str(i+1))
    solve(nums, i+1, res+' '+str(i+1))


T = int(input())
for _ in range(T):
    N = int(input())
    num = [i for i in range(1, N+1)]
    result = []

    solve(num, 1, '1')
    result.sort()
    for x in result:
        print(x)
    print()



# eval 사용했을 때. --> 근데 시간은 112ms로 더 많이 걸린다.. 왜?
def solve(nums, i, res):
    global result
    if i == nums[-1]:
        exp = res.replace(' ', '')
        if eval(exp)==0:
            result.append(res)
        return
    solve(nums, i+1, res+'+'+str(i+1))
    solve(nums, i+1, res+'-'+str(i+1))
    solve(nums, i+1, res+' '+str(i+1))


T = int(input())
for _ in range(T):
    N = int(input())
    num = [i for i in range(1, N+1)]
    result = []

    solve(num, 1, '1')
    result.sort()
    for x in result:
        print(x)
    print()