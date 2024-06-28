"""
문제 이름: 다이얼
문제 링크: https://www.acmicpc.net/problem/5622
문제 티어: 브론즈 2

타임라인
2024.06.27 10:23am~10:34am (11분)  total: 11분

<정리>
"""

dials = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
dic = {}
i = 3
for dial in dials:
    for ch in dial:
        dic[ch] = i
    i += 1

word = input()
answer = 0
for c in word:
    answer += dic[c]
print(answer)