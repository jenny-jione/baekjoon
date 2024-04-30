"""
문제 이름: N과 M (5)
문제 링크: https://www.acmicpc.net/problem/15654

타임라인
2024.04.30 4:00pm~4:10pm (10분)

정리
1. 한번 뽑은 건 안뽑음 (ex. 1 1 허용x) -> visited 필요
2. (1 7) (7 1)이 다름. -> 조합이 아니라 순열!
"""


N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()

visited = [0] * (10001)
seq = []

def solve():
    if len(seq)==M:
        print(' '.join(map(str, seq)))
        return
    for i in numbers:
        if not visited[i]:
            seq.append(i)
            visited[i] = 1
            solve()
            seq.pop()
            visited[i] = 0

solve()