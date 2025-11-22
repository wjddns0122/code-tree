has_cold_list = []
temp_list = []
count = 0

for i in range(3):
    has_cold, temp = input().split()  # 예: "Y 37.5"
    has_cold_list.append(has_cold)    # "Y" 또는 "N"
    temp_list.append(int(temp))     # 문자열 -> 실수로 변환


# 감기 있는 사람 수 세기
if has_cold_list[0] == "Y" and temp_list[0] >= 37:
    count += 1
if has_cold_list[1] == "Y" and temp_list[1] >= 37:
    count += 1
if has_cold_list[2] == "Y" and temp_list[2] >= 37:
    count += 1

if count >= 2:
    print("E")
else:
    print("N")