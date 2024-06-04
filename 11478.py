"""
문제 이름: 서로 다른 부분 문자열의 개수
문제 링크: https://www.acmicpc.net/problem/11478
문제 티어: 실버 3

타임라인
2024.06.04 02:26pm~02:29pm (3분)
"""

s = input().strip()
sub_str = set()
for i in range(len(s)):
    for j in range(i+1, len(s)+1):
        sub_str.add(s[i:j])
print(len(sub_str))