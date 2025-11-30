a, b, c = map(int, input().split())

# 기준 시각보다 이전인 경우
if a < 11:
    print(-1)
elif a == 11 and b < 11:
    print(-1)
elif a == 11 and b == 11 and c < 11:
    print(-1)
else:
    # 기준: 11일 11시 11분
    # 경과 분 = (날짜 차이 * 24 + 시 차이) * 60 + 분 차이
    elapsed_min = ((a - 11) * 24 + (b - 11)) * 60 + (c - 11)
    print(elapsed_min)
