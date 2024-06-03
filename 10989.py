"""
문제 이름: 수 정렬하기 3
문제 링크: https://www.acmicpc.net/problem/10989
문제 티어: 브론즈 1

타임라인
2024.06.03 11:38am~11:48am (10분)
2024.06.03 11:58am~12:10pm (12분)
2024.06.03 12:27pm~12:41pm (14분)

★☆★☆★ [필독] 수 정렬하기 3 FAQ ★☆★☆★
https://www.acmicpc.net/board/view/26132


단순하게 sort()를 썼다가 메모리초과가 난 후에,
시간 제한과 메모리 제한, 시간복잡도에 대해서 공부를 하게 된 문제.

도움이 되었던 힌트
1. 모든 입력을 배열에 저장하면 당연히 메모리 초과입니다.
    문제의 메모리 제한은 겨우 8MB입니다. 아무리 작은 자료형으로 저장한다고 해도
    short형(2byte) 천만 개면 약 20MB로 역시 메모리 초과입니다.
    입력을 전부 저장하지 않고 푸는 방법을 생각해보세요.
    힌트는 입력되는 정수의 범위에 있습니다.
2. 느린 입출력을 써도 시간 초과가 될 수 있습니다.
    [빠른 A+B] 문제에서 내가 충분히 빠른 입출력을 쓰고 있는지 확인해보세요.

나의 문제 풀이 방향
(실패) 무지성 sort() 사용
(통과) 딕셔너리 사용. key:숫자, value:그 숫자가 입력으로 들어온 개수
        그래서 1부터 10001까지 key에 있는 숫자를 value번 만큼 출력하면 된다.
"""

import sys
input = sys.stdin.readline

N = int(input())
my_dict = {}
for _ in range(N):
    n = int(input())
    my_dict.setdefault(n, 0)
    my_dict[n] += 1

for num in range(1, 10001):
    if num in my_dict:
        for _ in range(my_dict[num]):
            print(num)

"""
참고할 만한 다른 코드
setdefault를 쓰지 않고 리스트를 이용하는 방법도 있다.
"""

import sys
input = sys.stdin.readline

N = int(input())
arr = [0]*10001
for _ in range(N):
    n = int(input())
    arr[n] += 1

for n in range(1, 10001):
    if arr[n] > 0:
        for _ in range(arr[n]):
            print(n)
