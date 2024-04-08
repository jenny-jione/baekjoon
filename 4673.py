"""
문제 이름: 셀프 넘버
문제 링크: https://www.acmicpc.net/problem/4673

타임라인
2024.4.8 9:48pm~10:12pm (24분)
"""

NUM = 10000
creator = [0] * (NUM+1)
for n in range(1, NUM+1):
    chars = [int(c) for c in str(n)]
    dn = n + sum(chars)
    if dn <= NUM:
        creator[dn] += 1

for i in range(1, NUM+1):
    if creator[i] == 0:
        print(i)
