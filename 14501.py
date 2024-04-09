"""
문제 이름: 퇴사
문제 링크: https://www.acmicpc.net/problem/14501

타임라인
2024.4.8 11:38pm
~ 2024.4.9 7:45pm
계속 붙잡고 있느라 .. 3시간 붙잡고 있다가 결국 답 코드 봄
"""

n = int(input())
cs = []
for _ in range(n):
    t, p = map(int, input().split())
    cs.append((t, p))

# 내가 원하던 풀이 .. !
def consult(i, rev):
    global max_rev
    if i == n:
        max_rev = max(max_rev, rev)
        return
    # i일에 상담 안하는 경우 전날과 rev는 같음. 상담 안해서 idx일에 수입 0이므로.
    consult(i+1, rev)
    # 상담 가능한 경우 다음 날짜는 i + t
    if i + cs[i][0] <= n:
        consult(i+cs[i][0], rev+cs[i][1])

max_rev = 0
consult(0, 0)
print(max_rev)