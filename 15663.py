"""
문제 이름: N과 M (9)
문제 링크: https://www.acmicpc.net/problem/15663

타임라인
2024.04.30 

문제 정리
"같은 것이 있는 순열"
"""

# 같은 숫자가 있는걸 어떻게 다뤄야 할지 모르겠음.. 9a 9b 이렇게 붙여서 다루었더니 시간초과 남..
N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()
ndict = {}
for n in numbers:
    if n not in ndict:
        ndict[n] = 1
    else:
        ndict[n] += 1

numbers_abc = []
for num, cnt in ndict.items():
    for i in range(cnt):
        numbers_abc.append(str(num)+str(chr(i+97)))

seq = []
res = []

def solve():
    if len(seq)==M:
        res.append(seq[:])
        return
    for n in numbers_abc:
        if n not in seq:
            seq.append(n)
            solve()
            seq.pop()

solve()

result = []
for seq in res:
    new_seq = [e[:-1] for e in seq]
    if new_seq not in result:
        result.append(new_seq)
    
for s in result:
    print(' '.join(s))