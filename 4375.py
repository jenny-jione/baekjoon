"""
문제 이름: 1
문제 링크: https://www.acmicpc.net/problem/4375
문제 티어: 실버 3

타임라인
2024.08.16 09:50am~09:57am (7분)  total: 7분

<정리>
1. 입력의 종료 조건이 주어지지 않을 때
    while문과 try-except문으로 입력을 받는다.
"""

def solve(n: int):
    kn = 1
    ans = 1
    while True:
        if kn%n == 0:
            break
        kn = 10*kn + 1
        ans += 1
    return ans

while True:
    try:
        n = int(input())
        kn, ans = 1, 1
        while True:
            if kn%n == 0:
                break
            kn = 10 * kn + 1
            ans += 1
        print(ans)
    except:
        break
