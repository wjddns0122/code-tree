n = int(input())

cnt0 = 0  # 교실
cnt1 = 0  # 복도
cnt2 = 0  # 화장실

for i in range(1, n + 1):
    if i % 12 == 0:      # 가장 긴 주기 먼저!
        cnt2 += 1        # 화장실
    elif i % 3 == 0:     # 그 다음 3일마다
        cnt1 += 1        # 복도
    elif i % 2 == 0:     # 마지막으로 2일마다
        cnt0 += 1        # 교실
    # 아무 조건도 안 맞으면 그날은 청소 없음

print(cnt0, cnt1, cnt2)
