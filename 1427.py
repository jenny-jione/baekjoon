"""
문제 이름: 소트인사이드
문제 링크: https://www.acmicpc.net/problem/1427
문제 티어: 실버 V

타임라인
2024.06.03 02:11pm~02:14pm (3분)
"""

n = list(map(int, input()))
n.sort(reverse=True)
print(''.join(map(str, n)))


# 한 줄에 출력하는 다른 방법
for i in n:
    print(i, end='')