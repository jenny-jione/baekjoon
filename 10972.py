"""
문제 이름: 다음 순열
문제 링크: https://www.acmicpc.net/problem/10972
문제 티어: 실버 3

타임라인
2024.08.08 10:42am~11:26am (44분)
2024.08.08 11:39am~12:47pm (68분)  total: 112분

<정리>
1. itertools.permutation은 시간복잡도가 O(N!)이다.
    이 문제에서 N=10000이므로... ...
2. 파이썬에서 swap은 아주 쉽게 가능하다.
    a[3], a[4] = a[4], a[3]
"""

# 내 코드 (통과)
N = int(input())
s = list(map(int, input().split()))

def get_next(s: list):
    last = [i for i in range(N, 0, -1)]
    if s == last:
        print(-1)
        return
    k = 1
    for i in range(1, N):
        if s[-(i+1)] < s[-i]:
            break
        k += 1
    if k == 1:
        # head, tail = s[:-2], s[-2:][::-1]
        # print(*(s[:-2]+s[-2:][::-1]))
        # swap으로 아래처럼 훨씬 간편하게 쓸 수 있다.
        s[-2], s[-1] = s[-1], s[-2]
        print(*s)
        return
    else:
        # a: 바뀌지 않는 부분
        # 예를 들어 13254에서 a=13
        a = s[:-(k+1)]
        # b: 다음 순열을 위해 바뀌는 부분
        # 예를 들어 13254에서 254가 200대에서 가장 큰 수이므로 400대로 올라가야 함
        # 3은 이미 13에서 쓰였으므로 쓸 수 없음.
        # 그러므로 b=254
        b = s[-(k+1):]
        # old_head는 new_head를 위한 변수임.
        # 왜 old_head를 선언했냐면, 2(old_head)보다 크고 다른 수보다 작은 수가 new_head이기 때문.
        # 예를 들어 b=254에서 old_head는 2이고, new_head는 4임.
        old_head = b[0]
        # new_head를 위한 정렬
        b.sort()
        hidx = b.index(old_head)
        new_head = b[hidx+1]
        tail = [x for x in b if x != new_head]
        answer = a + [new_head] + tail
        print(*answer)
        return

get_next(s)