# 입력 받기
m1, d1, m2, d2 = map(int, input().split())
A = input()

# 각 달의 날짜 수 (2024년 윤년 기준)
num_of_days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

# 1월 1일부터 해당 날짜까지 총 며칠인지 세는 함수
def totalDay(m, d):
    num = 0
    for i in range(1, m):
        num += num_of_days[i]
    num += d
    return num

# 1. 두 날짜 사이의 간격 구하기
# 시작일도 포함해야 하므로 마지막에 +1을 하는 것이 맞습니다.
diff = totalDay(m2, d2) - totalDay(m1, d1) + 1

# 2. 요일 세기
count = 0

# 문제 조건: 시작일(m1, d1)은 무조건 월요일(=인덱스 0)
start_day_index = 0 

for i in range(diff):
    # 시작점(0)에서 하루씩 더해가며 요일 확인
    current_index = (start_day_index + i) % 7
    
    if week[current_index] == A:
        count += 1

print(count)