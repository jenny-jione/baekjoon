"""
문제 이름: Z
문제 링크: https://www.acmicpc.net/problem/1074
문제 티어: 골드 5

타임라인
2024.11.11 07:47pm~08:43pm (56분)  total: 56분

<정리>
1. 분할정복
2. 사분면 quadrant
"""

def kan(start, end, x):
    mid = (start + end) // 2
    if x >= mid:
        return (mid, end, 1)
    else:
        return (start, mid, 0)

N, r, c = map(int, input().split())
r_start, c_start = 0, 0
r_end, c_end = 2**N, 2**N
answer = 0
for i in range(N, 0, -1):
    r_start, r_end, row = kan(r_start, r_end, r)
    c_start, c_end, col = kan(c_start, c_end, c)
    answer += 4**i * (row*2+col) // 4

print(answer)