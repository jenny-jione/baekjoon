"""
문제 이름: 오큰수
문제 링크: https://www.acmicpc.net/problem/17298
문제 티어: 골드 4

타임라인
2024.07.15 02:45pm~03:16pm (31분)  total: 31분

<정리>
1. 리스트를 공백을 두고 한 줄로 출력하는 방법: print(*리스트)
2. if문의 조건과 while의 조건이 중복되는 것 같다면 줄일 수 있다.
"""

n = int(input())
arr = list(map(int, input().split()))
s = []
nge = [-1] * n
for i, x in enumerate(arr):
    if s and s[-1][0] < x:
        while s:
            if s[-1][0] < x:
                _, idx = s.pop()
                nge[idx] = x
            else:
                break
    s.append((x, i))
            
print(' '.join(map(str, nge)))


# 내 코드 개선 - if문과 while문에서 중복되는 조건을 하나로 합침
n = int(input())
arr = list(map(int, input().split()))
s = []
nge = [-1] * n
for i, x in enumerate(arr):
    while s and s[-1][0] < x:
        _, idx = s.pop()
        nge[idx] = x
    s.append((x, i))
            
print(' '.join(map(str, nge)))