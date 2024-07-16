"""
문제 이름: 후위 표기식2
문제 링크: https://www.acmicpc.net/problem/1935
문제 티어: 실버 3

타임라인
2024.07.16 11:33am~12:04pm (31분)  total: 31분

<정리>
1. 아스키코드 - A는 65임
2. 알파벳과 피연산자를 대응시키기 - 딕셔너리 없이 operand 만으로도 구현 가능.
    내 코드는 alpha_dict라는 딕셔너리를 구현해서 ('A':0, .. 'Z':25)
    그걸 다시 입력받은 operand의 인덱스로 넣었는데 쉬운 길을 일부러 돌아가는 코드였다.
    그냥 operand[ord(c)-65]로 구현하면 됨. 
3. 알파벳인지 확인
    1) c.isalpha()
    2) 'A' <= c <= 'Z'
    * isalpha(), isdigit(), isalnum()은 모두 '문자열'의 함수이다. (사실 당연함)
"""

# 내 코드 (통과)
n = int(input())
notation = list(input())
alpha_dict = {chr(i):i-65 for i in range(65, 65+26)}
operand = [int(input()) for _ in range(n)]
for i, x in enumerate(notation):
    if x not in '+-*/':
        notation[i] = operand[alpha_dict[x]]
s = []
for c in notation:
    if str(c).isdigit():
        s.append(c)
    else:
        if c == '+':
            b, a = s.pop(), s.pop()
            s.append(a+b)
        elif c == '-':
            b, a = s.pop(), s.pop()
            s.append(a-b)
        elif c == '*':
            b, a = s.pop(), s.pop()
            s.append(a*b)
        elif c == '/':
            b, a = s.pop(), s.pop()
            s.append(a/b)
print(format(s[-1], '.2f'))


# 개선한 코드
n = int(input())
expression = list(input())
operand = [int(input()) for _ in range(n)]

s = []
for c in expression:
    if 'A' <= c <= 'Z':
        s.append(operand[ord(c)-65])
    else:
        if c == '+':
            b, a = s.pop(), s.pop()
            s.append(a+b)
        elif c == '-':
            b, a = s.pop(), s.pop()
            s.append(a-b)
        elif c == '*':
            b, a = s.pop(), s.pop()
            s.append(a*b)
        elif c == '/':
            b, a = s.pop(), s.pop()
            s.append(a/b)
print(format(s[-1], '.2f'))
print('%.2f' %s[-1])