"""
문제 이름: 설탕배달
문제 링크: https://www.acmicpc.net/problem/2839

타임라인
2024.05.31 12:51pm~01:03pm (12분)

<정리>
1. 내가 쓴 방법은 정답이 전혀 아닌 경우도 반드시 순회하기 때문에 비효율적임.
2. while-else를 사용해보자
"""

N = int(input())

answer = 2000
five, three = N//5, N//3
for f in range(five+1):
    for t in range(three+1):
        if f*5+t*3==N:
            answer = min(answer, f+t)
if answer==2000:
    print(-1)
else:
    print(answer)


# 통과 후 참고해서 개선한 코드

sugar = int(input())
bag = 0
while sugar >= 0:
    if sugar%5 == 0:
        bag += sugar//5
        print(bag)
        break
    sugar -= 3
    bag += 1
else:
    print(-1)