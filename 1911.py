"""
문제 이름: 흙길 보수하기
문제 링크: https://www.acmicpc.net/problem/1911
문제 티어: 골드 5

타임라인
2024.10.30 11:47am~12:18pm (31분)  total: 31분

<정리>
1. 올림 나눗셈
    (웅덩이 크기, 널빤지 크기) = (5, 3)인 경우, 필요한 널빤지 개수는 2개임.
    (웅덩이 크기, 널빤지 크기) = (7, 3)인 경우, 필요한 널빤지 개수는 3개임.
    즉, 널빤지가 정확히 나눠떨어지지 않는 경우를 대비해
    (널빤지 크기-1) 를 더하면 필요한 널빤지의 개수를 정확히 구할 수 있음.
    (p+(L-1))//L
    (5+(3-1))//3 = 2
    (7+(3-1))//3 = 3
2. while문 대신 한번에 몫(나눗셈)으로 처리하기

"""
N, L = map(int, input().split())
puddles = sorted([list(map(int, input().split())) for _ in range(N)])

cnt = 0
x = puddles[0][0]
for p1, p2 in puddles:
    if x < p1:
        x = p1
    board = ((p2-x)+(L-1))//L
    cnt += board
    x += board * L
print(cnt)