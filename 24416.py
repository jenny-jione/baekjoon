"""
문제 이름: 알고리즘 수업 - 피보나치 수 1
문제 링크: https://www.acmicpc.net/problem/24416
문제 티어: 브론즈 1

타임라인
2024.06.14 11:26am~11:46am (20분)  total: 20분

<정리>
1. 동적 계획법. 동적 프로그래밍. Dynamic Programming
"""

N = int(input())

# cnt1, cnt2 = 0, 0
# def fib_recur(n):
#     global cnt1
#     if n==1 or n==2:
#         cnt1 += 1
#         return 1
#     else:
#         return fib_recur(n-1) + fib_recur(n-2)

code2 = 0
def fib_dp(n):
    global code2
    f = [0] * (n+1)
    f[1], f[2] = 1, 1
    if n<3:
        return f[n]
    for i in range(3, n+1):
        code2 += 1
        f[i] = f[i-1] + f[i-2]
    return f[n]

code1 = fib_dp(N)
print(code1, code2)