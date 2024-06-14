"""
문제 이름: 신나는 함수 실행
문제 링크: https://www.acmicpc.net/problem/9184
문제 티어: 실버 2

타임라인
2024.06.14 12:11pm~12:47pm (36분)
2024.06.14 01:05pm~01:25pm (20분)  total: 56분

<정리>
1. dp.
2. 나는 a,b,c의 범위가 1~20까지는 배열을 미리 초기화해두고 입력받은 다음에 배열 값을 반환했는데,
    다른 사람의 코드를 보니, 전부 0으로 초기화해 둔 다음에 값이 있으면 바로 리턴하고
    값이 없으면 arr[a][b][c]를 그 때 업데이트 하는 방식으로 했다. 그게 조금 더 간편한 것 같다.
"""

# 내 코드 - 통과
import sys
input = sys.stdin.readline

funny = [[[1] * 21 for _ in range(21)] for _ in range(21)]
for i in range(1, 21):
    for j in range(1, 21):
        for k in range(1, 21):
            if i<j and j<k:
                funny[i][j][k] = funny[i][j][k-1] + funny[i][j-1][k-1] - funny[i][j-1][k]
            else:
                funny[i][j][k] = funny[i-1][j][k] + funny[i-1][j-1][k] + funny[i-1][j][k-1] - funny[i-1][j-1][k-1]
answer = []
while True:
    a, b, c = map(int, input().strip().split())
    if a==-1 and b==-1 and c==-1:
        break
    if a<=0 or b<=0 or c<=0:
        result = 1
    elif a>20 or b>20 or c>20:
        result = funny[20][20][20]
    else:
        result = funny[a][b][c]
    answer.append([a, b, c, result])

for ans in answer:
    print(f'w({ans[0]}, {ans[1]}, {ans[2]}) = {ans[-1]}')



# 다른 코드
import sys
input = sys.stdin.readline

arr = [[[0] * 21 for _ in range(21)] for _ in range(21)]

def w(a, b, c):
    if a<=0 or b<=0 or c<=0:
        return 1
    if a>20 or b>20 or c>20:
        return w(20, 20, 20)
    if arr[a][b][c]:
        return arr[a][b][c]
    if a<b<c:
        arr[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
    else:
        arr[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
    return arr[a][b][c]

while True:
    a, b, c = map(int, input().strip().split())
    if a==-1 and b==-1 and c==-1:
        break
    print(f'w({a}, {b}, {c}) = {w(a, b, c)}')
