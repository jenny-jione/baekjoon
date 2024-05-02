"""
문제 이름: N과 M (10)
문제 링크: https://www.acmicpc.net/problem/15664

타임라인
2024.05.02 1:14pm~1:22pm (8분)

문제 정리
1. 비내림차순 -> 조합 -> for문 범위(재귀함수 매개변수로 정보 전달)
2. 같은 것이 있는 -> used 변수 사용(재귀함수의 불필요한 중복호출 방지)
"""

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()

visited = [0] * N
seq = []

def solve(start):
    if len(seq)==M:
        print(' '.join(map(str, seq)))
        return
    used = 0
    for i in range(start, N):
        number = numbers[i]
        if not visited[i] and used != number:
            visited[i] = 1
            seq.append(number)
            used = number
            solve(i)
            visited[i] = 0
            seq.pop()

solve(0)