"""
문제 이름: 블랙잭
문제 링크: https://www.acmicpc.net/problem/2798

타임라인
2024.05.30 03:03pm~03:19pm (16분)

<정리>
1. 그냥 단순하게 3중 for문 써도 됨
2. itertools.combinations을 써도 됨 .. 근데 코테에서 허용 안할 수도 있지 않나?
"""

N, M = map(int, input().split())
cards = list(map(int, input().split()))

visited = [0] * N
cnt = 0
answer = -1

def pick(cur, cnt, subsum):
    global answer
    if cnt == 3:
        if subsum <= M:
            answer = max(answer, subsum)
        return
    for i in range(cur+1, N):
        if not visited[i]:
            visited[i] = 1
            pick(i, cnt+1, subsum+cards[i])
            visited[i] = 0

pick(0, 0, 0)
print(answer)