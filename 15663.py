"""
문제 이름: N과 M (9)
문제 링크: https://www.acmicpc.net/problem/15663

타임라인
2024.04.30 5:00pm~5:20pm (20분)
2024.05.01 3:08pm~3:23pm (15분)
2024.05.01 4:00pm~4:45pm (45분)
2024.05.02 11:41am~12:21pm (40분)
--- 코드 참고 ---
2024.05.02 12:45pm~1:05pm (40분)

정리
"같은 것이 있는 순열" -> used 변수로 불필요한 재귀함수 호출 방지하기
1, 7, 9(1), 9(2)가 있을 때
(1, 1)을 거르는 방법 --> visited 배열
(1, 9(1)) (1, 9(2))를 거르는 방법 --> used 변수.
재귀함수에 들어가기 직전에 used = numbers[i]를 할당한다.
그러면 (1, 9(1))를 고른 뒤에는 used==9가 되어서 (1, 9(2))의 경우에는 재귀함수를 호출하지 않는다.
"""

# 같은 숫자가 있는걸 어떻게 다뤄야 할지 모르겠음.. 9a 9b 이렇게 붙여서 다루었더니 시간초과 남..
# N, M = map(int, input().split())
# numbers = list(map(int, input().split()))
# numbers.sort()

# ndict = {}
# for n in numbers:
#     if n not in ndict:
#         ndict[n] = 1
#     else:
#         ndict[n] += 1

# numbers_abc = []
# for num, cnt in ndict.items():
#     for i in range(cnt):
#         numbers_abc.append(str(num)+str(chr(i+97)))

# seq = []
# res = []

# def solve():
#     if len(seq)==M:
#         res.append(seq[:])
#         return
#     for n in numbers_abc:
#         if n not in seq:
#             seq.append(n)
#             solve()
#             seq.pop()

# solve()

# result = []
# for seq in res:
#     new_seq = [e[:-1] for e in seq]
#     if new_seq not in result:
#         result.append(new_seq)
    
# for s in result:
#     print(' '.join(s))

#####

"""
<핵심 아이디어>
1, 7, 9(1), 9(2)가 있을 때
(1, 1)을 거르는 방법 --> visited 배열
(1, 9(1)) (1, 9(2))를 거르는 방법 --> used 변수.
재귀함수에 들어가기 직전에 used = numbers[i]를 할당한다.
그러면 (1, 9(1))를 고른 뒤에는 used==9가 되어서 (1, 9(2))의 경우에는 재귀함수를 호출하지 않는다.
"""

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()

seq = []
visited = [0] * N

def solve():
    if len(seq)==M:
        print(' '.join(map(str, seq)))
        return
    used = 0
    for i in range(N):
        if not visited[i] and used!=numbers[i]:
            visited[i] = 1
            seq.append(numbers[i])
            used = numbers[i]
            solve()
            visited[i] = 0
            seq.pop()

solve()