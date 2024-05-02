"""
문제 이름: N과 M (6)
문제 링크: https://www.acmicpc.net/problem/15655

타임라인
2024.04.30 4:26pm~4:37pm (11분)

문제 정리
0. N개의 수에서 M개를 뽑는 조합 문제.
1. 조합 - (1 7)과 (7 1)은 같은 것으로 간주하여 (1 7)만 출력 - for문의 범위가 1부터가 아니라 자기 자신부터임.
2. 중복 허용 안함. - (1 1) 허용 안함. - visited 배열 필요.
3. for문에서 i는 numbers의 인덱스를 의미한다.
    (수정 전에는 numbers의 실제 수를 사용했는데 그게 코드를 더 복잡하게 만듦. 그래서 수정.)
"""

# 조합. (1 7)과 (7 1)은 같은 것으로 간주하여 (1 7)만 출력
# (1 1) 허용 안함. 중복 허용 안함. visited 필요.

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()
visited = [0] * N
seq = []

def solve(start):
    if len(seq)==M:
        print(' '.join(map(str, seq)))
        return
    for i in range(start, N):
        if not visited[i]:
            visited[i] = 1
            seq.append(numbers[i])
            solve(i)
            visited[i] = 0
            seq.pop()

solve(0)