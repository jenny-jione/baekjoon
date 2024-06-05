"""
문제 이름: 창문 닫기
문제 링크: https://www.acmicpc.net/problem/13909
문제 티어: 실버 5

타임라인
2024.06.05 12:00pm~12:15pm (15분)
2024.06.05 01:53pm~02:18pm (25분)

<정리>
1. 제곱수는 약수의 개수가 홀수이다! 이 아이디어를 떠올리면 코드가 매우 간단해짐
2. sqrt .. 도 좋지만 그냥 단순하게 n**0.5 를 하면 루트 n이 된다.
3. int() 함수는 파라미터가 실수일 경우 소수점 이하를 버린 후 반환한다.
    - 정수인 문자열을 정수로 반환한다. (정수가 아닐 경우 에러)
    - int(value, base)는 base진법인 문자열 value를 10진법 정수로 변환한다.
        value에는 문자열이 들어가야 함. 숫자는 x
"""

# 제곱 수 구하기 !
# 내가 통과한 코드
N = int(input())
i = 1
while True:
    if i*i >= N:
        if i*i > N:
            i -= 1
        break
    i += 1
print(i)


# 더 간단하게
N = int(input())
print(int(N**0.5))




### 통과 전까지 고민한 코드
# 시도 1
def get_divisor_count(k: int):
    cnt = 0
    for i in range(1, k//2 + 1):
        if k%i == 0:
            cnt += 1
    return cnt

N = int(input())

answer = 0
for i in range(1, N+1):
    if get_divisor_count(i) % 2 == 0:
        answer += 1
print(answer)



# 시도 2 (배수로 시도)
N = int(input())
windows = [0] * (N+1)
answer = 0
for i in range(1, N+1):
    for w in range(1, N+1):
        if w % i == 0:
            if windows[w] == 0:
                windows[w] = 1
                answer += 1
            else:
                windows[w] = 0
                answer -= 1
    print(windows)

print(answer)