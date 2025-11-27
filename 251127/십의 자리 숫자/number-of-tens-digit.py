arr = list(map(int, input().split()))

count_arr = [0] * 100
for elem in arr:
    if elem >= 10:
        elem = elem // 10
        count_arr[elem] += 1
    elif elem == 0:
        break

for i in range(1, 10):
    cnt = count_arr[i]
    print(f"{i} - {cnt}")