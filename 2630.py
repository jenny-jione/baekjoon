"""
문제 이름: 색종이 만들기
문제 링크: https://www.acmicpc.net/problem/2630
문제 티어: 실버 2

타임라인
2024.11.12 01:19pm~01:43pm (24분)  total: 24분

<정리>
1. 분할 정복
2. 재귀
3. base case (기저 사례)
    특정 구역이 한 가지 색으로만 이루어졌다면 해당 구역을 더 이상 분할하지 않고, 
    그 색의 카운트를 증가시켜 재귀 호출을 종료한다.
4. 4등분 분할
    쿼드 트리 (Quad Tree)
"""

# 내 코드
from collections import deque

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
answer = [0, 0]
dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

def check_color(y0, x0, length):
    q = deque([(y0, x0)])
    color = board[y0][x0]    
    visited = [[0] * length for _ in range(length)]
    visited[0][0] = 1
    while q:
        y, x = q.popleft()
        for yi, xi in zip(dy, dx):
            ny, nx = y+yi, x+xi
            if y0<=ny<y0+length and x0<=nx<x0+length and visited[ny-y0][nx-x0]==0:
                if board[ny][nx] != color:
                    return False
                else:
                    visited[ny-y0][nx-x0] = 1
                    q.append((ny, nx))
    return True

def search(y, x, length):
    if check_color(y, x, length):
        answer[board[y][x]] += 1
        return
    else:
        for i, j in zip([0, 0, 1, 1], [0, 1, 0, 1]):
            search(y+length//2*i, x+length//2*j, length//2)

search(0, 0, N)
print(*answer, sep='\n')


# 개선된 코드
"""
1. 리스트 언팩킹 제거
    for i, j in zip([0, 0, 1, 1], [0, 1, 0, 1])는 반복되는 리스트 언팩킹 연산임
    -> 변수로 상수화.
    directions = [(0, 0), (0, 1), (1, 0), (1, 1)]
    효과 1) zip 객체 생성 오버헤드를 줄일 수 있음.
        zip과 리스트 언팩킹이 매번 실행될 필요 없이 한 번 정의된 directions 리스트를 순회하면 된다.
    2) 가독성 증가
"""
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
answer = [0, 0]
directions = [(0, 0), (0, 1), (1, 0), (1, 1)]

def check_color(y, x, length):
    color = board[y][x]
    for yi in range(y, y+length):
        for xi in range(x, x+length):
            if board[yi][xi] != color:
                return False
    return True

def search(y, x, length):
    if check_color(y, x, length):
        answer[board[y][x]] += 1
        return
    for dy, dx in directions:
        search(y+length//2*dy, x+length//2*dx, length//2)

search(0, 0, N)
print(*answer, sep='\n')