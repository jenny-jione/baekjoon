"""
문제 이름: N과 M (6)
문제 링크: https://www.acmicpc.net/problem/15655

타임라인
2024.04.30 4:26pm~4:37pm (11분)

문제 정리
1. 조합 - (1 7)과 (7 1)은 같은 것으로 간주하여 (1 7)만 출력 - for문의 범위가 1부터가 아니라 자기 자신부터임.
2. 중복 허용 안함. - (1 1) 허용 안함. - visited 배열 필요.
"""

# 조합. (1 7)과 (7 1)은 같은 것으로 간주하여 (1 7)만 출력
# (1 1) 허용 안함. 중복 허용 안함. visited 필요.

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()
visited = [0] * 10001
seq = []

def solve(start):
    if len(seq)==M:
        print(' '.join(map(str, seq)))
        return
    for i in numbers[numbers.index(start):]:
        if not visited[i]:
            visited[i] = 1
            seq.append(i)
            solve(i)
            visited[i] = 0
            seq.pop()

solve(numbers[0])