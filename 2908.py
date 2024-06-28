"""
문제 이름: 상수
문제 링크: https://www.acmicpc.net/problem/2908
문제 티어: 브론즈 2

<정리>
1. 뒤집기 처리 -> [::-1]
2. 둘 중 큰 값 처리 -> max()함수
"""

# def reverse(s):
#     return int(''.join(list(reversed(s))))

# a, b = map(reverse, input().split())
# if a > b:
#     print(a)
# else:
#     print(b)

"""
개선점
1. 뒤집기 처리 -> [::-1]
2. 둘 중 큰 값 처리 -> max()함수
"""

# a, b = map(int, input()[::-1].split())
# print(max(a, b))


print(max(map(int, input()[::-1].split())))