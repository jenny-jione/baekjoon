"""
문제 이름: 한수
문제 링크: https://www.acmicpc.net/problem/1065

타임라인
2024.4.8 6:41pm~6:53pm (12분)
"""

n = int(input())

def hansu_check(k):
    strk = [int(c) for c in str(k)]
    if len(strk) <= 2:
        return True
    diff = strk[1] - strk[0]
    for k1, k2 in zip(strk[1:], strk[2:]):
        if k2 - k1 != diff:
            return False
    return True

answer = 0
for i in range(1, n+1):
    if hansu_check(i):
        answer += 1
print(answer)