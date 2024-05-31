"""
문제 이름: 영화감독 숌
문제 링크: https://www.acmicpc.net/problem/1436

타임라인
2024.05.31 12:23pm~12:29pm (6분)
2024.05.31 12:38pm~12:46pm (8분)
"""

N = int(input())

num = 0
movie = 666
while True:
    if '666' in str(movie):
        num += 1
    if num == N:
        print(movie)
        break
    movie += 1