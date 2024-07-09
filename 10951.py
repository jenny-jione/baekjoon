"""
문제 이름: A+B - 4
문제 링크: https://www.acmicpc.net/problem/10951
문제 티어: 브론즈 5

<정리>
1. EOF 다루기
2. 입력종료조건이 없는 문제 다루기
"""

while True:
    try:
        a, b = map(int, input().split())
        print(a+b)
    except:
        break

    