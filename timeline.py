"""
입력 예시
2
2117-2133
2148-2204

출력 예시
2024.MM.DD 09:17pm~09:33pm (16분)
2024.MM.DD 09:48pm~10:04pm (16분)
* MM.DD는 그날 날짜가 출력된다.

TODO
1. (완료) 총 걸린 시간도 마지막에 넣기
2. (완료) 출력에 아예 README.md 넣기
"""

from datetime import datetime, date
today = date.today().strftime('%Y.%m.%d')

def calculate(start_time_str, end_time_str):
    start_time = datetime.strptime(start_time_str, '%H%M')
    end_time = datetime.strptime(end_time_str, '%H%M')
    
    elasped_time = end_time - start_time

    start_time_result = start_time.strftime('%I:%M%p').lower()
    end_time_result = end_time.strftime('%I:%M%p').lower()

    elasped_minutes = elasped_time.total_seconds() / 60
    result = f'{today} {start_time_result}~{end_time_result} ({int(elasped_minutes)}분)'
    return result

N = int(input('Please enter multiple time ranges:'))

result = []
for _ in range(N):
    data = input()
    start, end = data.split('-')
    result.append(calculate(start, end))

print(f"""
\"\"\"
문제 이름: 
문제 링크: 
문제 티어: 

타임라인
{chr(10).join(result)}
\"\"\"
""")