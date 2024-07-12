"""
문제 이름: 에디터
문제 링크: https://www.acmicpc.net/problem/1406
문제 티어: 실버 2

타임라인
2024.07.12 11:20am~11:53am (33분)  total: 33분

<정리>
내 풀이
0. 커서의 앞과 뒤를 각각 다른 deque로 설정했다.
1. L 명령의 경우 q1 맨 뒤의 값을 q2 맨 앞에 붙이기
2. D 명령의 경우 q2 맨 앞의 값을 q1 맨 뒤에 붙이기
3. B 명령의 경우 q1 맨 뒤의 값 삭제
4. P 명령의 경우 q1 맨 뒤에 값 삽입

다른 사람의 풀이
0. 커서의 앞과 뒤를 각각 리스트로 설정
명령어 처리 부분은 거의 비슷.
단, 리스트는 popleft가 없기 때문에 커서 뒤의 리스트는 거꾸로 저장한다.
나중에 출력만 reversed로 하면 됨. (혹은 [::-1])
"""

# 내 코드 - deque 2개로 풂
import sys
from collections import deque
input = sys.stdin.readline

q1 = deque(input().rstrip())
q2 = deque([])
m = int(input().rstrip())
for _ in range(m):
    cmd = input().rstrip().split()
    if cmd[0] == 'L':
        if q1:
            x = q1.pop()
            q2.appendleft(x)
    elif cmd[0] == 'D':
        if q2:
            x = q2.popleft()
            q1.append(x)
    elif cmd[0] == 'B':
        if q1:
            q1.pop()
    else:
        q1.append(cmd[1])

print(''.join(list(q1))+''.join(list(q2)))


# 리스트 2개로 푼 코드
import sys
input = sys.stdin.readline

s1 = list(input().rstrip())
s2 = []
m = int(input().rstrip())
for _ in range(m):
    cmd = input().rstrip().split()
    if cmd[0] == 'L':
        if s1:
            x = s1.pop()
            s2.append(x)
    elif cmd[0] == 'D':
        if s2:
            x = s2.pop()
            s1.append(x)
    elif cmd[0] == 'B':
        if s1:
            s1.pop()
    else:
        s1.append(cmd[1])

print(''.join(s1)+''.join(s2[::-1]))