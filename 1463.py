"""
문제 이름: 1로 만들기
문제 링크: https://www.acmicpc.net/problem/1463
문제 티어: 실버 3

타임라인
2024.07.17 11:05am~11:37am (32분)  total: 32분

<정리>
1. dp라고 해서 점화식을 생각해낸건데 만약 문제유형 없었으면 어떻게 접근해야 할지 막막했었을듯
2. DP (Dynamic Programming) 동적 계획법
3. 탑다운과 바텀업
    1) Top-Down (하향식)
        큰 문제를 해결하기 위해 작은 문제를 호출하는 방식
        메모이제이션
            한 번 구한 결과를 메모리 공간에 메모해두고, 같은 식을 호출하면 메모한 결과를 그대로 가져오는 기법
        재귀함수 사용
        메모이제이션 처리 오버헤드 존재할 수 있음
    2) Bottom-Up (상향식)
        가장 작은 문제들로부터 답을 구해가며 전체 문제의 답을 찾는 방식
        반복문 이용
        재귀 호출x
        메모리 절약 효과 있음
"""

# 시간초과
answer = int(1e6)
def solve(x, cnt):
    global answer
    if x == 1:
        answer = min(cnt, answer)
        return
    if x%3==0:
        solve(x//3, cnt+1)
    if x%2==0:
        solve(x//2, cnt+1)
    solve(x-1, cnt+1)
    return
n = int(input())
solve(n, 0)
print(answer)


# 내 코드 (통과)
n = int(input())
arr = [-1, 0, 1, 1]
for i in range(4, n+1):
    cand = []
    if i%3==0:
        cand.append(arr[i//3]+1)
    if i%2==0:
        cand.append(arr[i//2]+1)
    cand.append(arr[i-1]+1)
    arr.append(min(cand))
print(arr[n])


# 조금 개선 (근데 내 코드랑 똑같지 않나..?)
n = int(input())
arr = [0] * (n+1)
for i in range(2, n+1):
    arr[i] = arr[i-1] + 1
    if i%3 == 0:
        arr[i] = min(arr[i], arr[i//3]+1)
    if i%2 == 0:
        arr[i] = min(arr[i], arr[i//2]+1)
print(arr[n])