"""
문제 이름: 베르트랑 공준
문제 링크: https://www.acmicpc.net/problem/4948
문제 티어: 실버 2

타임라인
2024.06.17 09:47pm~10:00pm (13분)
2024.06.17 10:10pm~10:15pm (5분)  total: 18분

<정리>
1. 미리 123456*2까지 소수인지 리스트에 저장해두고 나중에는 n~2n 사이에 sum만 하기
TODO: 에라토스테네스의 체를 이용해서도 풀기
"""

import sys
input = sys.stdin.readline

prime_number = [0, 0]

# 0으로 초기화 후 값 업데이트 vs 하나씩 append 중 뭐가 더 빠름?

def is_prime_number(n):
    if n==1:
        return False
    elif n==2:
        return True
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            return False
    return True

for i in range(2, 123456*2+1):
    prime_number.append(is_prime_number(i))

while True:
    n = int(input())
    if n==0:
        break
    print(sum(prime_number[n+1:n*2+1]))