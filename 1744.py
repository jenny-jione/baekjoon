"""
문제 이름: 수 묶기
문제 링크: https://www.acmicpc.net/problem/1744
문제 티어: 골드 4

타임라인
2024.10.24 10:34am~11:29am (55분)  total: 55분

<정리>
"""

# 내 코드
n = int(input())
pos, neg, zero = [], [], 0
for _ in range(n):
    x = int(input())
    if x == 0:
        zero += 1
    elif x > 0:
        pos.append(x)
    else:
        neg.append(x)

pos.sort(reverse=True)
neg.sort()

answer = 0
for i in range(0, len(pos)-1, 2):
    a, b = pos[i], pos[i+1]
    if a * b > a + b:
        answer += a * b
    else:
        answer += a + b
if len(pos)%2==1:
    answer += pos[-1]

for i in range(0, len(neg)-1, 2):
    answer += neg[i] * neg[i+1]
if len(neg)%2==1 and zero == 0:
        answer += neg[-1]

print(answer)



# 개선된 코드
n = int(input())
numbers = [int(input()) for _ in range(n)]

# 양수와 음수 분리 및 정렬
pos = sorted([x for x in numbers if x > 1], reverse=True)  # 1은 곱하면 손해이므로 제외
neg = sorted([x for x in numbers if x < 0])  # 음수는 오름차순으로 정렬
ones = numbers.count(1)  # 1은 그냥 더해주는 것이 유리
zero = numbers.count(0)  # 0의 개수 체크

answer = ones  # 1은 그냥 더해주기

# 양수 처리
for i in range(0, len(pos) - 1, 2):
    answer += pos[i] * pos[i + 1]
if len(pos) % 2 == 1:
    answer += pos[-1]

# 음수 처리
for i in range(0, len(neg) - 1, 2):
    answer += neg[i] * neg[i + 1]
if len(neg) % 2 == 1 and zero == 0:  # 0이 없으면 남은 음수 더하기
    answer += neg[-1]

print(answer)



# 개선2
n = int(input())
pos, neg = [], []
answer = 0
for _ in range(n):
    x = int(input())
    if x == 1:
        answer += 1
    elif x > 1:
        pos.append(x)
    else:
        neg.append(x)

pos.sort(reverse=True)
neg.sort()

for i in range(0, len(pos)-1, 2):
    answer += pos[i] * pos[i+1]
if len(pos)%2==1:
    answer += pos[-1]

for i in range(0, len(neg)-1, 2):
    answer += neg[i] * neg[i+1]
if len(neg)%2==1:
        answer += neg[-1]

print(answer)