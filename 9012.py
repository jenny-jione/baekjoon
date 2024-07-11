"""
문제 이름: 괄호
문제 링크: https://www.acmicpc.net/problem/9012
문제 티어: 실버 4

타임라인
2024.07.11 12:46pm~12:53pm (7분)  total: 7분

<정리>
1. 아이디어 - VPS라면 괄호 ()짝을 전부 소거시킬 수 있다.
2. replace로 없애면 된다. 언제까지? ()가 없을 때까지.
"""

# 내 풀이
def is_vps(ps: str):
    state = 0
    for c in ps:
        if c=='(':
            state += 1
        else:
            state -= 1
        if state < 0:
            return False
    if state == 0:
        return True
    else:
        return False

T = int(input())
for _ in range(T):
    ps = input().strip()
    if is_vps(ps):
        print('YES')
    else:
        print('NO')


# 다른 풀이 - replace로 ()를 소거하는 풀이
T = int(input())
for _ in range(T):
    ps = input()
    while '()' in ps:
        ps = ps.replace('()', '')
    if ps:
        print('NO')
    else:
        print('YES')
