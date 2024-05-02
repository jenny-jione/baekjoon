"""
문제 이름: N과 M (8)
문제 링크: https://www.acmicpc.net/problem/15657

타임라인
2024.04.30 4:51pm~4:55pm (4분)

문제 정리
1. N개 중에서 M개를 뽑는 중복조합 문제.
2. (1 1)인 수열 허용하므로 -> 중복 가능 문제 => visited 필요 없음
3. 비내림차순이므로 (1 7)은 ok, (7 1)은 no -> 조합 문제 => for문의 범위는 start 이상으로 계속 바뀜
4. for문에서 i는 numbers의 인덱스를 의미한다.
    (수정 전에는 numbers의 실제 수를 사용했는데 그게 코드를 더 복잡하게 만듦. 그래서 수정.)
5. solve 함수의 매개변수는 numbers의 인덱스이다.
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
    for i in range(start, N):
        seq.append(numbers[i])
        solve(i)
        seq.pop()

solve(0)