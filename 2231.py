"""
문제 이름: 분해합
문제 링크: https://www.acmicpc.net/problem/2231

타임라인
2024.4.8 10:20pm~10:32pm (12분)
"""


n = int(input())

generators = []
for i in range(1, n+1):
    chars = [int(c) for c in str(i)]
    gen = i + sum(chars)
    if gen == n:
        generators.append(i)

if not generators:
    print(0)
else:
    print(generators[0])


# 근데 애초에 1부터 시작하기 때문에 생성자 찾는 순간 그게 가장 작은 생성자임. 그래서 그 후는 안해도 됨.
# 예외처리만 제대로 해야 됨.. 생성자가 없는 경우 i가 n까지 가기 때문에 이 조건 거는게 중요 !!
# -- 수정 버전 --
n = int(input())

for i in range(1, n+1):
    chars = [int(c) for c in str(i)]
    gen = i + sum(chars)
    if gen == n:
        print(i)
        break
    if i == n:
        print(0)