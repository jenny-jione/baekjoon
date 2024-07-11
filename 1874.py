"""
문제 이름: 스택 수열
문제 링크: https://www.acmicpc.net/problem/1874
문제 티어: 실버 2

타임라인
2024.07.11 01:03pm~01:22pm (19분)
2024.07.11 11:10pm~11:29pm (19분)  total: 38분

<정리>
아래 코드로 통과는 했으나, 시간이 2844ms임. 가장 빠른 코드가 70ms정도이므로 ..
TODO: 더 효율적인 코드로 짜보기.
"""

n = int(input())
seq = [int(input()) for _ in range(n)]
stack = []
cur = 1
idx = 0
result = []
while True:
    if cur > n and not stack:
        break
    if cur > n and stack[-1] != seq[idx]:
        print('NO')
        result = []
        break
    if not stack or stack[-1]!=seq[idx]:
        stack.append(cur)
        result.append('+')
        cur += 1
    elif stack and stack[-1]==seq[idx]:
        stack.pop()
        result.append('-')
        idx += 1
if result:
    for res in result:
        print(res)