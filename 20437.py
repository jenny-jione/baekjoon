"""
문제 이름: 문자열 게임 2
문제 링크: https://www.acmicpc.net/problem/20437
문제 티어: 골드 5

타임라인
2024.10.14 11:56am~01:30pm (94분)  total: 94분

<정리>
1. 슬라이딩 윈도우
2. 인덱스 다루기!! 중요!! 첫값 끝값
3. setdefault
"""
T = int(input())
for _ in range(T):
    w = input().rstrip()
    k = int(input())

    alpha_count = {}
    for i in range(len(w)):
        alpha_count.setdefault(w[i], 0)
        alpha_count[w[i]] += 1
    
    alpha_index = {}
    for i in range(len(w)):
        if alpha_count[w[i]] >= k:
            alpha_index.setdefault(w[i], [])
            alpha_index[w[i]].append(i)
    
    result = []
    for idx_arr in alpha_index.values():
        for i in range(len(idx_arr)-k+1):
            result.append(idx_arr[i+k-1]-idx_arr[i]+1)
    
    if result:
        result.sort()
        print(result[0], result[-1])
    else:
        print(-1)