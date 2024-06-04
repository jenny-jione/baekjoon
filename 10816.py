"""
문제 이름: 숫자 카드 2
문제 링크: https://www.acmicpc.net/problem/10816
문제 티어: 실버 4

타임라인
2024.06.04 12:22pm~12:26pm (4분)

<정리>
1. if in 은 리스트보다 딕셔너리, set이 훨 씬 빠르다
2. -K ~ K 까지 다뤄야 한다면 리스트 2개보다 딕셔너리 하나를 사용하자. 어차피 in 은 빠름
"""


import sys
input = sys.stdin.readline

plus = [0] * 10000001
minus = [0] * 10000001
N = int(input())
my_card = list(map(int, input().strip().split()))
for i in my_card:
    if i > 0:
        plus[i] += 1
    else:
        minus[-i] += 1

M = int(input())
card = list(map(int, input().strip().split()))
for i in card:
    if i > 0:
        print(plus[i], end=' ')
    else:
        print(minus[-i], end=' ')


# 딕셔너리 이용
import sys
input = sys.stdin.readline

N = int(input().strip())
my_card = list(map(int, input().strip().split()))
M = int(input().strip())
card = list(map(int, input().strip().split()))

dic = {}
for i in my_card:
    dic.setdefault(i, 0)
    dic[i] += 1

for i in card:
    if i in dic:
        print(dic[i], end=' ')
    else:
        print(0, end=' ')