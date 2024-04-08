"""
문제 이름: 그룹 단어 체커
문제 링크: https://www.acmicpc.net/problem/1316

타임라인
2024.4.8 3:42pm~3:55pm (13분)
"""

n = int(input())
words = []
result = 0
for _ in range(n):
    word = input()
    leng = len(word)
    diff = 1
    chars = [word[0]]
    for i in range(leng-1):
        chars.append(word[i+1])
        if word[i] != word[i+1]:
            diff += 1
    kind = len(list(set(chars)))
    if diff == kind:
        result += 1
print(result)