"""
문제 이름: 이차원 배열과 연산
문제 링크: https://www.acmicpc.net/problem/17140
문제 티어: 골드 4

타임라인
2024.09.19 02:47pm~03:48pm (61분)
2024.09.19 04:01pm~04:30pm (29분)  total: 90분

<정리>
1. 이차원 배열을 파라미터로 넘기기
    copy.deepcopy(arr)
2. 2차원 배열에서 특정 열 추출하기
    list(zip(*a))[j] : j열 추출하기
    a = [
            [0, 1],
            [2, 3],
            [4, 5],
            [6, 7],
            [8, 9],
        ]
    -> 
    [0, 2, 4, 6, 8]
    [1, 3, 5, 7, 9]
3. 다중 조건으로 정렬하기
    sorted(), key=lambda x:(다중조건)
    예. 정렬 1조건: value 오름차순, 정렬 2조건: key 오름차순 이라면
    sorted(arr.items(), key=lambda x:(x[1], x[0]))
"""

import copy
r, c, k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(3)]

def count(arr):
    count_dict = {}
    for i in range(len(arr)):
        num = arr[i]
        if num == 0:
            continue
        count_dict.setdefault(num, 0)
        count_dict[num] += 1
    res = sorted(count_dict.items(), key=lambda x:(x[1], x[0]))
    result = []
    for i in range(len(res)):
        result.append(res[i][0])
        result.append(res[i][1])
    return result

def transform(arr):
    result = []
    for i in range(len(arr[0])):
        result.append(list(zip(*arr))[i])
    return result

def row_cal(x, rlen):
    new_a = []
    max_len = 0
    for i in range(rlen):
        row = count(x[i])
        if max_len < len(row):
            max_len = len(row)
        new_a.append(row)
    
    for i in range(rlen):
        for _ in range(len(new_a[i]), max_len):
            new_a[i].append(0)
    return new_a


answer = 0
while True:
    if r <= len(a) and c <= len(a[0]) and a[r-1][c-1] == k:
        break
    if answer > 100:
        answer = -1
        break
    rlen = len(a)
    clen = len(a[0])
    tmp = copy.deepcopy(a)
    if rlen >= clen:
        a = row_cal(tmp, rlen)
    else:
        tmp = transform(tmp)
        rlen = len(tmp)
        a = row_cal(tmp, rlen)
        a = transform(a)
    answer += 1

print(answer)

"""
2
1447-1548
1601-1630
"""