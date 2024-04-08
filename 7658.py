"""
문제 이름: 덩치
문제 링크: https://www.acmicpc.net/problem/7568

타임라인
2024.4.8 6:23pm~6:38pm (15분)
"""

n = int(input())
body = []
for _ in range(n):
    x, y = map(int, input().split())
    body.append((x, y))

rank = [1] * n
for i in range(n):
    for j in range(i, n):
        if body[i][0] > body[j][0] and body[i][1] > body[j][1]:
            rank[j] += 1
        elif body[i][0] < body[j][0] and body[i][1] < body[j][1]:
            rank[i] += 1

print(' '.join(map(str, rank)))