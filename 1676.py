"""
문제 이름: 팩토리얼 0의 개수
문제 링크: https://www.acmicpc.net/problem/1676
문제 티어: 실버 5

타임라인
2024.07.16 03:22pm~04:00pm (38분)  total: 38분

<정리>
1. n은 5의 배수가 n//5개이다.
    ex. 100은 5, 10, 15, ..., 100 -> 100//5 == 20개
    ex. 99는 99//5 == 19개
2. 5의 제곱수들은 5의 지수만큼 5를 가지고 있다.
    ex. 25 = 5 * 5
    ex. 125 = 5 * 5 * 5
    따라서 제곱수일 때마다 5가 기존에서 하나씩 더해진다.
3. while문과 //, % 같이 쓰는거 아직 까다롭게 느껴진다 . . 
"""

# 내 풀이
n = int(input())

def get_five(k):
    result = 0
    while k>=5:
        if k%5==0:
            result += 1
            k //= 5
        else:
            break
    return result

answer = 0
for i in range(0, n+1, 5):
    if i==0:
        continue
    answer += get_five(i)
print(answer)


# 참고 풀이
n = int(input())
print(n//5 + n//25 + n//125)