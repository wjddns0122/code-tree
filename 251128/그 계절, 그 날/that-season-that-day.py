y, m, d = map(int, input().split())

def is_leap(year):
    # 윤년 판별
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

def is_valid_date(year, month, day):
    # 월 범위 체크
    if not (1 <= month <= 12):
        return False

    # 윤년 여부에 따라 2월 일수 변경
    if is_leap(year):
        days_in_month = [0,
                         31, 29, 31, 30, 31, 30,
                         31, 31, 30, 31, 30, 31]
    else:
        days_in_month = [0,
                         31, 28, 31, 30, 31, 30,
                         31, 31, 30, 31, 30, 31]

    last = days_in_month[month]

    # 일 범위 체크
    return 1 <= day <= last

def get_season(month):
    if month in (3, 4, 5):
        return "Spring"
    elif month in (6, 7, 8):
        return "Summer"
    elif month in (9, 10, 11):
        return "Fall"
    else:  # 12, 1, 2
        return "Winter"

# 먼저 날짜가 말이 되는지부터 검사
if not is_valid_date(y, m, d):
    print(-1)
else:
    season = get_season(m)
    print(season)
