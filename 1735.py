"""
문제 이름: 분수 합
문제 링크: https://www.acmicpc.net/problem/1735
문제 티어: 실버 3

타임라인
2024.06.13 03:07pm~03:25pm (18분)
2024.06.13 03:27pm~03:29pm (2분)  total: 20분

<정리>
1. 다음에 써야 할 변수를 함부로 바꾸지 말것
    ja //= math.gcd(ja, mo) 했다가 그 다음줄에서 잘못됨ㅎ
2. gcd . . 유클리드 호제법 . . 
"""

import math

a, b = map(int, input().split())
c, d = map(int, input().split())

ja = a*d + b*c
mo = b*d
div = math.gcd(ja, mo)
print(ja//div, mo//div)