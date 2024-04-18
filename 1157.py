"""
문제 이름: 단어 공부
문제 링크: https://www.acmicpc.net/problem/1157

타임라인
2024.4.18 10:45pm~10:52pm (7분)
"""

word = input().upper()
chars = [c for c in word]
unique = list(set(chars))
frequency = [(chars.count(u), u) for u in unique]
frequency.sort(reverse=True)
if len(frequency)>1 and frequency[0][0] == frequency[1][0]:
    print('?')
else:
    print(frequency[0][1])