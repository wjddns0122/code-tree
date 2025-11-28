M, D = map(int, input().split())

def is_valid_date(M, D):
    # 1. 월 범위 체크
    if not (1 <= M <= 12):
        return False

    # 2. 각 달의 마지막 날 정의
    days_in_month = [0,  # 0번 인덱스 더미
                     31, 28, 31, 30, 31, 30,
                     31, 31, 30, 31, 30, 31]

    last = days_in_month[M]

    # 3. 일 범위 체크
    if 1 <= D <= last:
        return True
    else:
        return False

if is_valid_date(M, D):
    print("Yes")
else:
    print("No")
