"""
문제 이름: 외판원 순회 2
문제 링크: https://www.acmicpc.net/problem/10971
문제 티어: 실버 2

타임라인
2024.08.12 10:05am~10:21am (16분)
2024.08.12 10:43am~10:48am (5분)  total: 21분

<정리>
1. 시간을 줄이기 위해서, 일반적인 종료조건 이외에 더 추가할 수 있는 조건이 있다면 추가하기.
    => 방문 도중에 현재까지의 최솟값보다 클 경우는 더이상 조사할 필요가 없음.
        ex) 5개 도시중에 현재까지의 최솟값이 50인데,
        3번째 도시 방문 중에 비용이 51이라면, 
        더이상 진행할 이유가 없음.
2. visied[j]=1, visited[j]=0 코드는 재귀함수 호출 직전 직후에 작성.
    1) 그러면 최초 방문지는 언제 1, 0으로 할당해야 하는지?
    2) 최초 방문지를 정하는 for문 안에서 하면 됨. (40~43라인 참고)
"""

N = int(input())
city = [list(map(int, input().split())) for _ in range(N)]
cnt = 0
answer = 10000001
visited = [0] * N
def solve(start, i, cnt, money):
    global answer
    # 방문중인 비용이 현재 answer보다 크다면, 굳이 더 방문할 필요가 없다.
    if money > answer:
        return
    if cnt == N and city[i][start] > 0:
        answer = min(money+city[i][start], answer)
        return
    for j in range(N):
        if not visited[j] and city[i][j] > 0:
            visited[j] = 1
            solve(start, j, cnt+1, money+city[i][j])
            visited[j] = 0

for i in range(N):
    visited[i] = 1
    solve(i, i, 1, 0)
    visited[i] = 0
print(answer)