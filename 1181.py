"""
문제 이름: 단어 정렬
문제 링크: https://www.acmicpc.net/problem/1181
문제 티어: 실버 V

타임라인
2024.06.03 03:22pm~03:28pm (6분)

< 정리 >
1. dic과 set은 시간면에서 비슷함. (832ms, 844ms)
2. not in 리스트 vs set은 3배 넘게 차이 (2888ms, 844ms)
3. sys.stdin.readline을 하면 1/10으로 시간이 단축됨. (844ms -> 64ms)
결론.
not in 리스트 << dic ~= set <<<< sys.stdin.readline
"""

N = int(input())
my_dict = {}
for _ in range(N):
    word = input()
    my_dict.setdefault(word, 0)
    my_dict[word] = len(word)
sorted_dic = sorted(my_dict.items(), key=lambda x:(x[1], x[0]))
for item in sorted_dic:
    print(item[0])
# 832ms


# 다른 풀이 .. 근데 더 오래 걸림;;ㅎㅎ
"""
set과 in list 중에 set이 더 효율적인 건가?
"""
N = int(input())
word_len = [[] for _ in range(51)]
for _ in range(N):
    word = input()
    if word not in word_len[len(word)]:
        word_len[len(word)].append(word)

for i in range(1, 51):
    if len(word_len[i])==0:
        continue
    for word in sorted(word_len[i]):
        print(word)
# 2888ms


# 출력 개선
N = int(input())
word_set_list = [[] for _ in range(51)]
for _ in range(N):
    word = input()
    if word not in word_set_list[len(word)]:
        word_set_list[len(word)].append(word)

for word_set in word_set_list:
    if len(word_set)==0:
        continue
    sorted_word_set = sorted(word_set)
    print('\n'.join(sorted_word_set))
# 2544ms


# word_len을 리스트 -> set
N = int(input())
word_set_list = [set() for _ in range(51)]
for _ in range(N):
    word = input()
    word_set_list[len(word)].add(word)

for word_set in word_set_list:
    if len(word_set)==0:
        continue
    sorted_word_set = sorted(word_set)
    print('\n'.join(sorted_word_set))
# 844ms


# sys.stdin.readline 사용
import sys
input = sys.stdin.readline

N = int(input().rstrip())
word_set_list = [set() for _ in range(51)]
for _ in range(N):
    word = input().rstrip()
    word_set_list[len(word)].add(word)

for word_set in word_set_list:
    if len(word_set)==0:
        continue
    sorted_word_set = sorted(word_set)
    print('\n'.join(sorted_word_set))
# 64ms