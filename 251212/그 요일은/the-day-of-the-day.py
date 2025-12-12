import sys

# 입력 받기
m1, d1, m2, d2 = map(int, input().split())
A = input()

# 각 달의 날짜 수 (2024년 윤년 기준)
num_of_days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# 작성하신 리스트 (0:Mon ~ 6:Sun)
week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

# [1] 날짜 수 세는 함수 (기존과 동일)
def totalDay(m, d):
    num = 0
    for i in range(1, m):
        num += num_of_days[i]
    num += d
    return num

# [2] 첼러의 공식 함수 (시작 요일을 구하기 위해 추가)
def get_real_weekday(year, month, day):
    if month <= 2:
        month += 12
        year -= 1
    q = day
    K = year % 100
    J = year // 100
    # 첼러 공식: 0=토, 1=일, 2=월, 3=화, 4=수, 5=목, 6=금
    h = (q + (13 * (month + 1)) // 5 + K + (K // 4) + (J // 4) - (2 * J)) % 7
    return h

# --- 메인 로직 변경 부분 ---

# 1. 시작 날짜의 '진짜' 요일 구하기 (2024년 기준)
zeller_idx = get_real_weekday(2024, m1, d1)

# 2. 첼러 인덱스(0=토)를 작성하신 week 리스트 인덱스(0=Mon)로 변환
# 첼러: 토(0), 일(1), 월(2), 화(3), 수(4), 목(5), 금(6)
# week: 월(0), 화(1), 수(2), 목(3), 금(4), 토(5), 일(6)
# 규칙: (첼러값 + 5) % 7 을 하면 week 인덱스와 맞아떨어집니다.
# 예) 월요일: 첼러(2) -> (2+5)%7 = 0 (Mon) -> 일치!
start_day_index = (zeller_idx + 5) % 7

# 3. 기간 구하기 (기존과 동일)
elapsed_day = totalDay(m2, d2) - totalDay(m1, d1) + 1

# 4. 반복문 돌면서 카운트 (기존과 동일)
count = 0
for i in range(elapsed_day):
    # 시작 요일 인덱스에서 i만큼 더하며 순회
    current_index = (start_day_index + i) % 7
    if week[current_index] == A:
        count += 1

print(count)