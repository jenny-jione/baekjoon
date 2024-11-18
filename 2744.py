"""
문제 이름: 대소문자 바꾸기
문제 링크: https://www.acmicpc.net/problem/2744
문제 티어: 브론즈 5

타임라인
2024.11.18 03:40pm~03:41pm (1분)  total: 1분

<정리>
upper() : 문자열의 알파벳을 전부 대문자로
lower() : 문자열의 알파벳을 전부 소문자로
swapcase() : 대문자 <-> 소문자
title() : 단어의 제일 앞 글자만 대문자로
"""

word = input()
result = ''
for ch in word:
    if 'a'<=ch<='z':
        result += chr(ord(ch)-32)
    else:
        result += chr(ord(ch)+32) 
print(result)