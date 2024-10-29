"""
문제 이름: 초콜릿 식사
문제 링크: https://www.acmicpc.net/problem/2885
문제 티어: 실버 2

타임라인
2024.10.29 10:38pm~11:06pm (28분)  total: 28분

<정리>
1. shift 연산
    a <<= 1
    a *= 2
    는 같은 동작을 한다.
2. 2의 보수
3. AND 연산
4. bin 함수
    결과값이 문자열.
    bin(100) == '0b1100100'
5. bin(k & -k)
    k의 이진 표현에서 가장 오른쪽에 있는 1비트를 추출하는 연산
"""

# 내 코드
choco_size = int(input())
d2 = 1
while d2 <= choco_size:
    d2 *= 2

d1 = d2 // 2

if d1 == choco_size:
    choco_size = d1
    cnt = 0
else:
    choco_size = d2
    cnt = 0
    while True:
        if d1 == choco_size:
            cnt += 1
            break
        if d1 > choco_size:
            d1 //= 2
            d2 //= 2
            cnt += 1
        else:
            choco_size -= d1

print(choco_size, cnt)


# 개선 (시프트 연산, 2의 보수, &연산, bin 사용)
k = int(input())
choco_size = 1
while choco_size < k:
    choco_size <<= 1
print(choco_size, len(bin(choco_size)) - len(bin(k & -k)))