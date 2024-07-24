"""
문제 이름: 2진수 8진수
문제 링크: https://www.acmicpc.net/problem/1373
문제 티어: 브론즈 1

타임라인
2024.07.23

<정리>
1. 진법이 나오면 일단 int(), bin(), oct(), hex()를 기억하자
2. 2, 8, 16진법은 서로 변환이 아주 쉽다
"""

# 내 코드
n = input()
length = len(n)
dic = {
    '000':'0',
    '001':'1',
    '010':'2',
    '011':'3',
    '100':'4',
    '101':'5',
    '110':'6',
    '111':'7',
}
if length % 3 == 0:
    answer = []
    b = n
else:
    f, b = n[:length%3], n[length%3:]
    answer = [dic[f.zfill(3)]]
for i in range(0, len(b)-1, 3):
    answer.append(dic[b[i:i+3]])
print(''.join(answer))


# 간결 풀이
n = int(input(), 2)
answer = oct(n)[2:]
print(answer)