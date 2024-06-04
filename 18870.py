"""
문제 이름: 좌표 압축
문제 링크: https://www.acmicpc.net/problem/18870
문제 티어: 실버 2

타임라인
2024.06.03 04:29pm~04:43pm (14분)

<정리>
1. list.index(i)는 시간복잡도 O(N)
    매번 최대 1,000,000번 수행하면서 시간초과.
2. 대신 딕셔너리를 사용하자. 시간복잡도가 O(1)임.
3. 딕셔너리 컴프리헨션도 손에 익혀두자. 코드가 간결해짐.
4. sorted는 매개변수로 들어온 이터러블한 데이터를 새로 정렬된 '리스트'로 반환해준다.
"""

# 통과한 코드
import sys
input = sys.stdin.readline

N = int(input().rstrip())
coord = list(map(int, input().strip().split()))
num_set = list(set(coord))
num_set.sort()
my_dict = {}
for idx, num in enumerate(num_set):
    my_dict[num] = idx

for x in coord:
    print(my_dict[x], end=' ')


# 코드 개선 - 딕셔너리 컴프리헨션
import sys
input = sys.stdin.readline

N = int(input().rstrip())
coord = list(map(int, input().strip().split()))
num_set = sorted(set(coord))

my_dict = {num_set[idx]:idx for idx in range(len(num_set))}

for x in coord:
    print(my_dict[x], end=' ')