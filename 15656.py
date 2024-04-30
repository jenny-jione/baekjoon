"""
문제 이름: N과 M (7)
문제 링크: https://www.acmicpc.net/problem/15656

타임라인
2024.04.30 4:41pm~4:46pm (5분)

문제 정리
1. 중복 허용 (1 1) => visited 필요 없음
2. 순열. => (1 7) (7 1) 둘 다 출력. => for문 범위는 항상 numbers 전체.
"""

# 중복 허용 => visited 필요없음
# (1 7) (7 1) 둘 다 출력. => 순열.

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()
seq = []

def solve():
    if len(seq)==M:
        print(' '.join(map(str, seq)))
        return
    for i in numbers:
        seq.append(i)
        solve()
        seq.pop()

solve()