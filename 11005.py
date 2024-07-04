"""
문제 이름: 진법 변환 2
문제 링크: https://www.acmicpc.net/problem/11005
문제 티어: 브론즈 1

타임라인
2024.07.04 09:42pm~09:54pm (12분)  total: 12분

<정리>
1. 딕셔너리 컴프리핸션 한번 써봄.
2. 문자열로도 해보고 리스트로도 해봄
3. 문자열 뒤집기를 인덱싱으로 할 수 있음.
    s[::-1]을 하면 reverse됨.
    근데 이게 제일 오래걸리네; 코드가 단순한 대신 시간은 더 걸림
4. 내가 base_dict라는 딕셔너리로 구현한 부분을
    단순하게 '01234...XYZ' 문자열로 선언한 다음
    나머지 값을 인덱스로 접근하는 방법이 있었음!!
"""

# 내 코드 - 통과
n, b = map(int, input().split())
base_dict = {i-55:chr(i) for i in range(65, 91)}
answer = ''
while n>0:
    x = n % b
    if x>9:
      answer = base_dict[x] + answer
    else:
      answer = str(x) + answer
    n //= b
print(answer)


# 리스트로
n, b = map(int, input().split())
base_dict = {i-55:chr(i) for i in range(65, 91)}
answer = []
while n>0:
    x = n % b
    if x>9:
        answer.append(base_dict[x])
    else:
        answer.append(str(x))
    n //= b
print(''.join(list(reversed(answer))))


# [::-1] 참고
# 문자열에도 인덱싱을 할 수 있다.
n, b = map(int, input().split())
base_dict = {i-55:chr(i) for i in range(65, 91)}
answer = ''
while n>0:
    x = n % b
    if x>9:
      answer += base_dict[x]
    else:
      answer += str(x)
    n //= b
print(answer[::-1])


# 참고
n, b = map(int, input().split())
s = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
answer = ''
while n>0:
    answer += s[n%b]
    n //= b
print(answer[::-1])