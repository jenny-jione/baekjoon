"""
문제 이름: N과 M (11)
문제 링크: https://www.acmicpc.net/problem/15665

타임라인
2024.05.02 1:39pm~1:49pm (10분)

문제 정리
1. 둘째 줄에 주어지는 N개의 수에 중복이 들어있음 --> set으로 중복 제거
2. 같은 수를 여러 번 골라도 된다 --> 중복허용 --> visited 필요 없음
3. (1 7) (7 1)은 다른 것으로 간주 --> 순열 --> for문 범위는 항상 전체
4. 중복순열 문제.
"""

n, m = map(int, input().split())
numbers = list(set(map(int, input().split())))
numbers.sort()

seq = []

def solve():
    if len(seq)==m:
        print(' '.join(map(str, seq)))
        return
    for i in range(len(numbers)):
        seq.append(numbers[i])
        solve()
        seq.pop()

solve()