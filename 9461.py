"""
문제 이름: 파도반 수열
문제 링크: https://www.acmicpc.net/problem/9461
문제 티어: 실버 3

타임라인
2024.06.16 11:20am~11:30am (10분)  total: 10분

<정리>
1. 점화식
2. N 범위가 1~100이므로 미리 배열을 초기화해도 된다.
"""

# 내 코드 - 통과
padovan = [0] * 101
for i in range(1, 4):
    padovan[i] = 1
for i in range(4, 6):
    padovan[i] = 2

def solve(n):
    if n<=5:
        return padovan[n]
    for i in range(6, n+1):
        padovan[i] = padovan[i-1] + padovan[i-5]
    return padovan[n]

T = int(input())
for _ in range(T):
    n = int(input())
    print(solve(n))


# 통과 후 개선한 코드 - 처음부터 100까지 구해놓기
padovan = [0, 1, 1, 1, 2, 2]
for i in range(6, 101):
    padovan.append(padovan[i-1]+padovan[i-5])

T = int(input())
for _ in range(T):
     n = int(input())
     print(padovan[n])