"""
문제 이름: N과 M (8)
문제 링크: https://www.acmicpc.net/problem/15657

타임라인
2024.04.30 4:51pm~4:55pm (4분)

문제 정리
1. 중복조합 문제.
2. (1 1)인 수열 허용하므로 -> 중복 가능 문제 => visited 필요 없음
3. 비내림차순이므로 (1 7)은 ok, (7 1)은 no -> 조합 문제 => for문의 범위는 start 이상으로 계속 바뀜
"""

# 중복조합
# 1 1 허용하므로 중복
# 비내림차순이므로 조합 (1 7은 o, 7 1은 x)

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()
seq = []

def solve(start):
    if len(seq)==M:
        print(' '.join(map(str, seq)))
        return
    for i in numbers[numbers.index(start):]:
        seq.append(i)
        solve(i)
        seq.pop()

solve(numbers[0])