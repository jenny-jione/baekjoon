"""
문제 이름: 조합 0의 개수
문제 링크: https://www.acmicpc.net/problem/2004
문제 티어: 실버 2

타임라인
2024.08.06 02:04pm~02:41pm (37분)  total: 37분

<정리>
1. 끝자리 0의 개수는 인수 10의 개수를 구하는 것과 같다.
2. 10은 2와 5의 곱이다.
3. 분모의 인수 10의 개수 - 분자의 인수 10의 개수
4. (분모의 인수 5의 개수 - 분자의 인수 5의 개수)
    vs (분모의 인수 2의 개수 - 분자의 인수 2의 개수) 중에
    더 작은 값으로 10이 만들어진다.
5. nCm = n! / {(n-m)! * m!}
"""

# 통과 코드
n, m = map(int, input().split())

def get_five_k(n):
    if n < 5:
        return 0
    k = 1
    while True:
        if 5**k <= n < 5**(k+1):
            break
        k += 1
    return k

def get_two_k(n):
    if n < 2:
        return 0
    k = 1
    while True:
        if 2**k <= n < 2**(k+1):
            break
        k += 1
    return k

five, two = 0, 0
ak5, ak2 = get_five_k(n), get_two_k(n)
for i in range(1, ak5+1):
    five += n//(5**i)
for i in range(1, ak2+1):
    two += n//(2**i)

bk5, bk2 = get_five_k(n-m), get_two_k(n-m)
for i in range(1, bk5+1):
    five -= (n-m)//(5**i)
for i in range(1, bk2+1):
    two -= (n-m)//(2**i)

ck5, ck2 = get_five_k(m), get_two_k(m)
for i in range(1, ck5+1):
    five -= m//(5**i)
for i in range(1, ck2+1):
    two -= m//(2**i)

print(min(five, two))


# 개선
n, m = map(int, input().split())
def get_count(n, k):
    if n < k:
        return 0
    cnt = 0
    while True:
        cnt += n//k
        n //= k
        if n < k:
            break
    return cnt

five = get_count(n, 5) - get_count(n-m, 5) - get_count(m, 5)
two = get_count(n, 2) - get_count(n-m, 2) - get_count(m, 2)
print(min(five, two))
