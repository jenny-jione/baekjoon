"""
문제 이름: 용액
문제 링크: https://www.acmicpc.net/problem/2467
문제 티어: 골드 5

타임라인
2024.10.14 02:05pm~02:40pm (35분)
2024.10.14 03:39pm~04:07pm (28분)  total: 63분

<정리>
1. 투 포인터
2. 투포인터와 이분탐색은 다르다!
    투포인터: O(N)
    이분탐색: O(logN)
"""

# 시간초과
# import sys
# input = sys.stdin.readline

# N = int(input().rstrip())
# lq = list(map(int, input().rstrip().split()))

# def solve():
#     val = 2000000001
#     for i in range(N):
#         for j in range(i+1, N):
#             mix = abs(lq[i] + lq[j])
#             if mix < val:
#                 val = mix
#                 result = [lq[i], lq[j]]
#             if mix == 0:
#                 return result
#     return result

# answer = solve()
# print(*sorted(answer))


import sys
input = sys.stdin.readline

N = int(input())
lq = list(map(int, input().rstrip().split()))
left, right = 0, N-1
M = 1000000000
lq1, lq2 = -M, M
min_val = 2*M+1
while left < right:
    val = lq[left] + lq[right]
    if abs(val) < min_val:
        lq1, lq2 = lq[left], lq[right]
        min_val = abs(val)
    if val > 0:
        right -= 1
    elif val < 0:
        left += 1
    else:
        break

print(lq1, lq2)