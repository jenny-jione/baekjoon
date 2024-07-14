"""
문제 이름: 단어 뒤집기 2
문제 링크: https://www.acmicpc.net/problem/17413
문제 티어: 실버 3

타임라인
2024.07.13 04:02pm~04:17pm (15분)
2024.07.14 10:27pm~10:33pm (6분)  total: 21분

<정리>
"""

s = input()
is_tag = False
tag = ''
stack = []
answer = ''
for c in s:
    if c== '<':
        is_tag = True
        while stack:
            answer += stack.pop()
        answer += '<'
    elif c == '>':
        is_tag = False
        answer += tag + '>'
        tag = ''
    else:
        if is_tag:
            tag += c
        else:
            if c == ' ':
                while stack:
                    answer += stack.pop()
                answer += ' '
            else:
                stack.append(c)
while stack:
    answer += stack.pop()
print(answer)