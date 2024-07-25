"""
문제 이름: 날짜 계산
문제 링크: https://www.acmicpc.net/problem/1476
문제 티어: 실버 5

타임라인
2024.07.25 02:28pm~03:12pm (44분)
2024.07.25 04:45pm~04:53pm (8분)  total: 52분

<정리>
0. 나머지를 이용하지만 완벽한 나머지는 아님.
1. E(1~15)는 Y=16이면 1이다.
2. S(1~28)는 Y=29이면 1이다.
3. M(1~19)는 Y=20이면 1이다.
"""

# 내 풀이
E, S, M = map(int, input().split())
y = 1
while True:
    e = y % 15 if y % 15 > 0 else 15
    s = y % 28 if y % 28 > 0 else 28
    m = y % 19 if y % 19 > 0 else 19
    if (e, s, m) == (E, S, M):
        print(y)
        break
    y += 1


# 다른 풀이
"""
e, s, m을 +1 해주면서 E, S, M이 될 때까지 반복한다.
e, s, m이 각각 15, 28, 19를 넘어가는 경우 다시 1로 돌아오게 한다.
끝!
"""
E, S, M = map(int, input().split())
e, s, m, year = 1, 1, 1, 1
while True:
    if (e, s, m) == (E, S, M):
        break
    year += 1
    e += 1
    s += 1
    m += 1
    if e > 15:
        e = 1
    if s > 28:
        s = 1
    if m > 19:
        m = 1
print(year)