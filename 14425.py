"""
문제 이름: 문자열 집합
문제 링크: https://www.acmicpc.net/problem/14425
문제 티어: 실버 4

타임라인
2024.06.04 11:25am~11:36am (11분)

<정리>
1. if in 을 사용할 때, list보다 set과 dict이 훨 씬 빠르다.
"""

# 내 코드 (근데 이러면 시간초과라는데 나는 통과함) 4620ms
N, M = map(int, input().split())
s = []
for _ in range(N):
    s.append(input())

answer = 0
for _ in range(M):
    string = input()
    if string in s:
        answer += 1

print(answer)


# set을 이용한 코드 - 훨씬 빠름. 616ms
N, M = map(int, input().split())
s = set()
for _ in range(N):
    s.add(input())

answer = 0
for _ in range(M):
    string = input()
    if string in s:
        answer += 1

print(answer)