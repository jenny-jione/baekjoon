"""
문제 이름: 치킨 배달
문제 링크: https://www.acmicpc.net/problem/15686
문제 티어: 골드 5

타임라인
2024.06.12 01:29pm~01:56pm (27분)
2024.06.12 02:04pm~02:10pm (6분)  total: 33분

<정리>
1. 백트래킹. 치킨집 M개를 뽑는게 먼저.
2. 치킨집 M개를 뽑았다면, 그 때의 도시의 치킨 거리를 구한다.
3. 도시의 치킨 거리의 최솟값을 업데이트하면 끝.
4. 치킨집 M개를 뽑는 것은 조합이기 때문에 for문의 범위 시작이 start부터임.
"""

N, M = map(int, input().split())
board = []
chicken, home = [], []
for i in range(N):
    board.append(list(map(int, input().split())))
    for j in range(N):
        if board[i][j] == 1:
            home.append((i, j))
        elif board[i][j] == 2:
            chicken.append((i, j))

visited = [0] * len(chicken)
answer = int(1e9)
pick = []

def solve(cnt, start):
    global answer
    if cnt == M:
        city_cd = 0
        for hy, hx in home:
            cd = 100
            for cy, cx in pick:
                cd = min(cd, abs(hy-cy)+abs(hx-cx))
            city_cd += cd
        answer = min(answer, city_cd)
        return
    for idx in range(start, len(chicken)):
        if not visited[idx]:
            i, j = chicken[idx]
            visited[idx] = 1
            pick.append((i, j))
            solve(cnt+1, idx)
            visited[idx] = 0
            pick.pop()
solve(0, 0)
print(answer)