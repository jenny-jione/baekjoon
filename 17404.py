"""
문제 이름: RGB거리 2
문제 링크: https://www.acmicpc.net/problem/17404
문제 티어: 골드 4

타임라인
2024.07.22 04:39pm~04:46pm (7분)
2024.07.22 05:01pm~05:43pm (42분)
2024.07.23 09:32am~10:02am (30분)  total: 79분

<정리>
1. 1번 집을 각각 R, G, B로 미리 칠했다고 생각한다.
    1. 만약 1번 집을 R로 칠했을 경우, G와 B를 선택하지 않게 하기 위해서
        1번 집의 빨강 비용을 제외한 다른 비용을 모두 선택할 수 없는 값으로 설정한다. (1000001)
    2. n번 집의 경우 빨간 색으로 칠할 수 없게 하기 위해서 n번 집의 빨강 비용을 선택할 수 없는 큰 값으로 설정한다.
    3. 다 끝나고 나면 설정해뒀던 값을 원래 값으로 복구시킨다. (왜냐면 G, B도 똑같은 과정을 거쳐야 하므로)
    4. 이걸 R, G, B 3번 반복한다.
2. 1001이 아니라 1000001인 이유: 1001이어도 그 앞에서 최솟값을 구하다보면 1001이 선택될 수 있음.
    1000001로 하게 되면, 1000개의 집의 모든 비용이 1000이어도 1000*1000 < 1000001 임.
3. 큰값은 상수로 설정해두자. 0이 너무 많아서 작성하면서 헷갈림!
4. R, G, B도 0, 1, 2 말고 변수로 설정해서 변수를 쓰자. 이것도 쓰다가 헷갈림.
"""

n = int(input())
a = [[0, 0, 0]] + [list(map(int, input().split())) for _ in range(n)]
answer = 1000001
dp = [[0, 0, 0] for _ in range(n+1)]
for color in range(3):
    rgb = a[1]
    a[1] = [1000001, 1000001, 1000001]
    a[1][color] = rgb[color]
    dp[1] = a[1]
    ncolor = a[n][color]    
    a[n][color] = 1000001
    for i in range(2, n+1):
        dp[i][0] = a[i][0] + min(dp[i-1][1], dp[i-1][2])
        dp[i][1] = a[i][1] + min(dp[i-1][2], dp[i-1][0])
        dp[i][2] = a[i][2] + min(dp[i-1][0], dp[i-1][1])
    a[n][color] = ncolor
    a[1] = rgb
    answer = min(answer, dp[n][0], dp[n][1], dp[n][2])
print(answer)


"""
<개선한 부분>
1. 1000001을 INF라는 변수로 설정함.
2. R, G, B를 기존에는 0, 1, 2로 숫자로 접근했는데, 혼란을 막기 위해 (작성하는 동안에도 헷갈림) 변수를 설정해줌.
3. 2~n for문 돌기 전에 a[n][color]값을 미리 큰값으로 바꿔두고 for문이 끝나면 원상복귀 시키는 것에서 
    → for문 다 돌고 나서 dp[n][color] 값을 INF로 업데이트하도록 변경.
    1. 개선 전의 코드: n에서 애초에 1번집의 색깔을 고르지 못하게 했었음
    2. 개선 후의 코드: 일단 n에서도 1번집의 색깔을 고를 수 있게 한 다음 그걸 INF로 무효화시킴.
"""
INF = 1000*1000 + 1
R, G, B = 0, 1, 2
n = int(input())
a = [[0, 0, 0]] + [list(map(int, input().split())) for _ in range(n)]
answer = INF
for color in range(3):
    dp = [[0, 0, 0] for _ in range(n+1)]
    dp[1] = [INF, INF, INF]
    dp[1][color] = a[1][color]
    for i in range(2, n+1):
        dp[i][R] = a[i][R] + min(dp[i-1][G], dp[i-1][B])
        dp[i][G] = a[i][G] + min(dp[i-1][B], dp[i-1][R])
        dp[i][B] = a[i][B] + min(dp[i-1][R], dp[i-1][G])
    dp[n][color] = INF
    answer = min(answer, dp[n][0], dp[n][1], dp[n][2])
print(answer)