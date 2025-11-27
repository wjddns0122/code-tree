arr = list(map(int, input().split()))
count_arr = [0] * 101

for elem in arr:
    elem = (elem // 10) * 10
    count_arr[elem] += 1
    if elem == 0:
        break

for i in range(100, 0, -10):
    cnt = count_arr[i]
    print(f"{i} - {cnt}")