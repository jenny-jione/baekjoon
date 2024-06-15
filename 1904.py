"""
문제 이름: 01타일
문제 링크: https://www.acmicpc.net/problem/1904
문제 티어: 실버 3

타임라인
2024.06.14 02:07pm~02:14pm (7분)
2024.06.14 02:23pm~03:01pm (38분)
--- 코드와 설명 봄 ---
2024.06.15 10:44pm~11:02pm (18분)  total: 63분

<정리>
1. %15746을 마지막에만 해주는 것이 아니라, 매번 점화식에서 취해준다. 오버플로우 방지를 위해.
    ** 100만번째 피보나치 수의 실제 값은 약 20만 "자리"의 수이다.
2. 점화식. dp.
3. n자리 이진수열은 n-1자리 이진수열에 1을 추가한 것 + n-2자리 이진수열에 00을 추가한 것과 같다. => 점화식
"""


N = int(input())

def solve(n):
    if n < 3:
        return n
    tile = [0] * (n+1)
    tile[1] = 1
    tile[2] = 2
    for i in range(3, n+1):
        tile[i] = (tile[i-1] + tile[i-2])%15746
    return tile[n]

print(solve(N))


"""
만일 덧셈으로만 이루어진 식에서 마지막 값의 1의 자리의 수를 구한다고 하면,
10의 자리 이상은 무시하고 1의 자리만 계속 유지하면서 진행해도 됩니다.
그것은 중간 결과를 계속 10으로 나눈 나머지를 가지고 진행하는 것과 같습니다.
마찬가지로, 15746진법으로 수를 표현해서 진행할 때 마지막 1의 자리의 수를 구하는 것이 목표라면
마지막 1의 자리만 유지하면서 진행해도 되고, 이는 15746으로 나눈 나머지를 가지고 진행하는 것과 같습니다.
-> https://www.acmicpc.net/board/view/41130
"""