"""
문제 이름: 스택 2
문제 링크: https://www.acmicpc.net/problem/28278
문제 티어: 실버 4

타임라인
2024.06.17 09:34pm~09:42pm (8분)  total: 8분
"""

import sys
input = sys.stdin.readline

stack = []
N = int(input())
for _ in range(N):
    data = list(map(int, input().rstrip().split()))
    if len(data)==2:
        stack.append(data[1])
    else:
        command = data[0]
        if command==2:
            if stack:
                print(stack.pop())
            else:
                print(-1)
        elif command==3:
            print(len(stack))
        elif command==4:
            if not stack:
                print(1)
            else:
                print(0)
        else:
            if stack:
                print(stack[-1])
            else:
                print(-1)


# stack에 넣는 원소는 굳이 정수형일 이유가 없음. -> map 안써도 됨.
import sys
input = sys.stdin.readline

stack = []
N = int(input())
for _ in range(N):
    command = input().rstrip().split()
    if command[0]=='1':
        stack.append(command[1])
    elif command[0]=='2':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif command[0]=='3':
        print(len(stack))
    elif command[0]=='4':
        if not stack:
            print(1)
        else:
            print(0)
    else:
        if stack:
            print(stack[-1])
        else:
            print(-1)