"""
문제 이름: N과 M (4)
문제 링크: https://www.acmicpc.net/problem/15652

타임라인
2024.04.30 3:53pm~3:56pm (3분)

정리
1. 비내림차순이 결국 조합이라는 뜻! 1 2는 출력하고 2 1은 출력하지 않으므로.
2. 중복해서 뽑기 허용 & 비내림차순 --> 중복조합을 의미함.
"""
# 비내림차순 a1<=a2<=a3<= .. <=ak-1<=ak

N, M = map(int, input().split())
seq = []

def solve(start):
    if len(seq)==M:
        print(' '.join(map(str, seq)))
        return
    for i in range(start, N+1):
        seq.append(i)
        solve(i)
        seq.pop()

solve(1)