"""
문제 이름: 스도쿠
문제 링크: https://www.acmicpc.net/problem/2580
문제 티어: 골드 4

타임라인
2024.06.11 12:03pm~12:28pm (25분)
2024.06.11 12:37pm~01:31pm (54분)
2024.06.11 02:59pm~03:55pm (56분)

<정리>
1. 백트래킹은 "원상복구" 해야 한다 !
2. 그 전에 방문한 곳은 가면 안되지! not visited 혹은 check==0으로 판단해야지.
    안그러면 간 곳 또 가고 또 가고 또 가고 .. (이래서 틀림)
3. if not visited and is_promising():
        visited = True
        재귀함수 호출
        visited = False
4. exit(0)은 프로그램 자체를 종료한다. 답이 여러개인데 하나만 출력하고 싶을 경우 사용.
    [2580] python에서 exit(0)과 return의 차이점
        https://www.acmicpc.net/board/view/80914
"""


board = []
zero_info = []
flag = False

idx = 0
for i in range(9):
    board.append(list(map(int, input().split())))
    for j in range(9):
        if board[i][j] == 0:
            zero_info.append([i, j])
            idx += 1

def is_promising(y, x, cand):
    if cand in board[y]:
        return False
    for row in range(9):
        if cand == board[row][x]:
            return False
    y0, x0 = y//3, x//3
    for gy in range(y0*3, (y0+1)*3):
        for gx in range(x0*3, (x0+1)*3):
            if cand == board[gy][gx]:
                return False
    return True

def sudoku(depth):
    global flag
    if flag:
        return
    if depth==len(zero_info):
        flag = True
        # 스도쿠 판 출력
        for i in range(9):
            print(' '.join(map(str, board[i])))
        return
    y, x = zero_info[depth]
    for i in range(1, 10):
        if board[y][x]==0 and is_promising(y, x, i):
            board[y][x] = i
            sudoku(depth+1)
            board[y][x] = 0
sudoku(0)


####


# 구글링 후 코드 개선
# exit 사용, 3x3 그룹 확인할 때 조금 더 간결하게 바꿈.
board = []
zero_info = []

idx = 0
for i in range(9):
    board.append(list(map(int, input().split())))
    for j in range(9):
        if board[i][j] == 0:
            zero_info.append([i, j])
            idx += 1

def is_promising(y, x, cand):
    if cand in board[y]:
        return False
    for row in range(9):
        if cand == board[row][x]:
            return False
    for i in range(3):
        for j in range(3):
            if cand == board[(y//3)*3+i][(x//3)*3+j]:
                return False
    return True

def sudoku(depth):
    if depth==len(zero_info):
        # 스도쿠 판 출력
        for i in range(9):
            print(' '.join(map(str, board[i])))
        exit()
    y, x = zero_info[depth]
    for i in range(1, 10):
        if board[y][x]==0 and is_promising(y, x, i):
            board[y][x] = i
            sudoku(depth+1)
            board[y][x] = 0
sudoku(0)



"""
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0


1 3 5 4 6 9 2 7 8
7 8 2 1 3 5 6 4 9
4 6 9 2 7 8 1 3 5
3 2 1 5 4 6 8 9 7
8 7 4 9 1 3 5 2 6
5 9 6 8 2 7 4 1 3
9 1 7 6 5 2 3 8 4
6 4 3 7 8 1 9 5 2
2 5 8 3 9 4 7 6 0
"""