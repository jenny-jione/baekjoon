"""
문제 이름: 회문
문제 링크: https://www.acmicpc.net/problem/17609
문제 티어: 골드 5

타임라인
2024.10.31 01:42pm~02:20pm (38분)
2024.10.31 05:19pm~05:47pm (28분)
2024.10.31 09:31am~09:37am (6분)  total: 72분

<정리>
1. 문자열
2. 투 포인터
"""

def check_pelindrome(substr):
    return substr == substr[::-1]

def solve(s):
    left, right = 0, len(s)-1
    while left < right:
        if s[left] != s[right]:
            if check_pelindrome(s[left+1:right+1]) or check_pelindrome(s[left:right]):
                return 1
            else:
                return 2
        left += 1
        right -= 1
    return 0

T = int(input())
for _ in range(T):
    print(solve(input()))