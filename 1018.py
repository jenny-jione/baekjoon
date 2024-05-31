"""
문제 이름: 체스판 다시 칠하기
문제 링크: https://www.acmicpc.net/problem/1018

타임라인
2024.05.31 10:54am~11:18am (24분)
2024.05.31 11:28am~11:57am (29분)

<정리>
1. i와 j를 일일이 짝홀 판단할 필요 없이 (i+j)를 판별하면 코드가 간결해진다.
2. 중복되는 부분은 줄이자.
    내 코드에서 paint_w, paint_b를 완성하는 for문은 결국 뒤의 min_val 구하는 for문과 중복됨.
3. 칠하는 횟수는 최대가 32임.
4. 제출 전에 안 쓰는 변수는 제거하기.
"""

N, M = map(int, input().split())
bw = 'BW'
board = []
for _ in range(N):
    board.append(list(input()))

paint_w = [[0]*M for _ in range(N)]
paint_b = [[0]*M for _ in range(N)]

# 0,0이 B인 경우: 짝수행은 짝수열이 W, 홀수열이 B, 홀수행은 짝수열이 B, 홀수열이 W
for i in range(N):
    for j in range(M):
        cell = board[i][j]
        if i%2==0:
            if j%2==0:
                if cell!='W':
                    paint_w[i][j] = 1
                else:
                    paint_b[i][j] = 1
            else:
                if cell!='B':
                    paint_w[i][j] = 1
                else:
                    paint_b[i][j] = 1
        else:
            if j%2==0:
                if cell!='B':
                    paint_w[i][j] = 1
                else:
                    paint_b[i][j] = 1
            else:
                if cell!='W':
                    paint_w[i][j] = 1
                else:
                    paint_b[i][j] = 1

min_val = 65
for y0 in range(N-8+1):
    for x0 in range(M-8+1):
        cnt1, cnt2 = 0, 0
        for i in range(y0, y0+8):
            for j in range(x0, x0+8):
                cnt1 += paint_w[i][j]
                cnt2 += paint_b[i][j]
        min_val = min([min_val, cnt1, cnt2])
       
print(min_val)


# 통과 후 개선한 코드. 코드 길이가 절반으로 줄었다!

N, M = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(input()))
min_val = 32
for y0 in range(N-8+1):
    for x0 in range(M-8+1):
        paint1, paint2 = 0, 0
        for i in range(y0, y0+8):
            for j in range(x0, x0+8):
                if (i+j)%2==0:
                    if board[i][j]!='W':
                        paint1 += 1
                    else:
                        paint2 += 1
                else:
                    if board[i][j]!='B':
                        paint1 += 1
                    else:
                        paint2 += 1
        min_val = min([min_val, paint1, paint2])
print(min_val)