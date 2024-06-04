"""
문제 이름: 통계학
문제 링크: https://www.acmicpc.net/problem/2108
문제 티어: 실버 3

타임라인
2024.06.04 02:34pm~02:54pm (20분)
2024.06.04 03:19pm~03:25pm (6분)
"""

import sys
input = sys.stdin.readline

N = int(input().strip())
nums = []
dic = {}
for _ in range(N):
    n = int(input().strip())
    nums.append(n)
    dic.setdefault(n, 0)
    dic[n] += 1
nums.sort()

result = [0] * 4
result[0] = round(sum(nums)/N)
result[1] = nums[N//2]

a = sorted(dic.items(), key=lambda x:(-x[1], x[0]))
if len(a) == 1:
    result[2] = a[0][0]
elif len(a) > 1 and a[0][1]==a[1][1]:
    result[2] = a[1][0]
else:
    result[2] = a[0][0]

result[3] = nums[-1] - nums[0]

for r in result:
    print(r)