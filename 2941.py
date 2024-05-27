"""
문제 이름: 크로아티아 알파벳
문제 링크: https://www.acmicpc.net/problem/2941

타임라인
2024.5.27 9:17pm~9:33pm (16분)
2024.5.27 9:48pm~10:04pm (16분)
"""

word = input()
idx = 0
answer = 0
res = []
while idx<len(word):
    ch = word[idx]
    if ch=='c' and idx+1<len(word) and word[idx+1] in '=-':
        res.append(word[idx:idx+2])
        answer += 1
        idx += 2
    elif ch=='d' and idx+2<len(word) and word[idx+1:idx+3]=='z=':
        res.append(word[idx:idx+3])
        answer += 1
        idx += 3
    elif ch=='d' and idx+1<len(word) and word[idx+1]=='-':
        res.append(word[idx:idx+2])
        answer += 1
        idx += 2
    elif idx+1<len(word) and word[idx+1]=='j' and ch in 'ln':
        res.append(word[idx:idx+2])
        answer += 1
        idx += 2
    elif idx+1<len(word) and word[idx+1]=='=' and ch in 'sz':
        res.append(word[idx:idx+2])
        answer += 1
        idx += 2
    else:
        res.append(word[idx])
        answer += 1
        idx += 1
print(answer)