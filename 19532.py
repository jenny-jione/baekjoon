"""
문제 이름: 수학은 비대면강의입니다
문제 링크: https://www.acmicpc.net/problem/19532

타임라인
2024.05.31 10:38am~10:43am (5분)
"""

a, b, c, d, e, f = map(int, input().split())

for x in range(-999, 1000):
    for y in range(-999, 1000):
        if a*x + b*y == c and d*x + e*y == f:
            print(x, y)
            break


# 2 - 근의 공식 활용 - 시간복잡도 O(1)
y = (a*f-c*d)//(a*d)-(b*d)