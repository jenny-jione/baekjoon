"""
문제 이름: 쇠막대기
문제 링크: https://www.acmicpc.net/problem/10799
문제 티어: 실버 2

타임라인
2024.07.15 02:27pm~02:41pm (14분)  total: 14분

<정리>
"""

data = input().replace('()', '0')
part = 0
answer = 0
for c in data:
    if c == '(':
        part += 1
    elif c == ')':
        part -= 1
        answer += 1
    else:
        answer += part
print(answer)