"""
문제 이름: N과 M (12)
문제 링크: https://www.acmicpc.net/problem/15666

타임라인
2024.05.02 2:00pm~2:03pm (3분)

문제 정리
1. 중복조합 문제
2. 입력으로 중복이 들어오기 때문에 set로 걸러주는 작업만 하면 단순한 중복조합 문제가 된다.
3. n != len(numbers)가 되므로 이것만 주의.
4. solve의 매개변수는 numbers의 인덱스이다. (비내림차순을 위한 것)
"""


n, m = map(int, input().split())
numbers = list(set(map(int, input().split())))
numbers.sort()

seq = []

def solve(start_idx):
    if len(seq)==m:
        print(' '.join(map(str, seq)))
        return
    for idx in range(start_idx, len(numbers)):
        seq.append(numbers[idx])
        solve(idx)
        seq.pop()

solve(0)