"""
문제 이름: 숨바꼭질
문제 링크: https://www.acmicpc.net/problem/1697

타임라인
2024.4.8 1:10pm~3:21pm (131분)
"""

n, k = map(int, input().split())
visited = [0] * 200001
visited[n] = 1
line = [(n, 0)]
pos = n

def move(pos, sec):
    result = []
    new_pos = [pos-1, pos+1, 2*pos]
    for np in new_pos:
        if np < 0:
            continue
        if np > n+k+1:
            continue
        if visited[np] == 0:
            result.append(np)
            visited[np] = 1
    return [result, sec+1]

cur = 0
sec = 0
flag = 0

while(not flag):
    if pos == k:
        print(sec)
        break
    newpos, newsec = move(pos, sec)
    for np in newpos:
        print(np, newsec)
        line.append((np, newsec))
    cur += 1
    pos = line[cur][0]
    sec = line[cur][1]
