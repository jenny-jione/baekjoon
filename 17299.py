"""
문제 이름: 오등큰수
문제 링크: https://www.acmicpc.net/problem/
문제 티어: 골드 3

타임라인
2024.07.15 03:32pm~03:52pm (20분)  total: 20분

<정리>
1. 오큰수의 응용문제
2. 인덱스 다루기
"""


n = int(input())
arr = list(map(int, input().split()))
f = {}
for x in arr:
    f.setdefault(x, 0)
    f[x] += 1
freq = [0] * n
for i in range(n):
    freq[i] = f[arr[i]]

stack = []
ngf = [-1] * n
for i, x in enumerate(freq):
    while stack and stack[-1][0] < x:
        _, idx = stack.pop()
        ngf[idx] = arr[i]
    stack.append((x, i))
print(*ngf)