"""
문제 이름: 대표값2
문제 링크: https://www.acmicpc.net/problem/2587
문제 티어: 브론즈 2

타임라인
2024.06.03 11:27am~11:29am (2분)
"""

nums = []
for _ in range(5):
    nums.append(int(input()))

nums.sort()
avg = sum(nums)//5
mid = nums[2]

print(avg)
print(mid)