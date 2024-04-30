"""
문제 이름: N과 M (1)
문제 링크: https://www.acmicpc.net/problem/15649

타임라인
2024.04.30 2:53pm~3:08pm (15분)

정리
1. int인 리스트를 한 줄에 공백 넣어서 출력하기 => join과 map 사용!
2. 백트래킹
  1) '다시 돌아간다' == 재귀함수 호출 전에 설정한 조건을 호출 후에는 되돌린다.
  2) 유망성 판단 <--dfs와의 차이점
"""

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
visited = [0] * (N+1)
sequence = []

def backtrack():
    if len(sequence)==M:
        print(' '.join(map(str, sequence)))
        return
    
    for i in range(1, N+1):
        if not visited[i]:
            visited[i] = 1
            sequence.append(i)
            backtrack()
            visited[i] = 0
            sequence.pop()
    
backtrack()