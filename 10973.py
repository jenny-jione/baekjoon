"""
문제 이름: 이전 순열
문제 링크: https://www.acmicpc.net/problem/10973
문제 티어: 실버 3

타임라인
2024.08.09 09:46am~10:16am (30분)  total: 30분

<정리>
"""

N = int(input())
s = list(map(int, input().split()))

def get_previous(s: list):
    first = [i for i in range(1, N+1)]
    if first == s:
        return -1
    if s[-2] > s[-1]:
        s[-2], s[-1] = s[-1], s[-2]
        return s
    k = -1
    for i in range(N-2, -1, -1):
        if s[i] > s[i+1]:
            break
        k -= 1
    a = s[:k-1]
    head = s[k-1]
    b = s[k-1:]
    b.sort(reverse=True)
    hidx = b.index(head)
    new_head = b[hidx+1]
    tail = [x for x in b if x != new_head]
    return a + [new_head] + tail

result = get_previous(s)
if result == -1:
    print(result)
else:
    print(' '.join(map(str, result)))