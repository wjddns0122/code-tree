arr = list(map(int, input().split()))

count_arr = [0] * 10
for elem in arr:
    count_arr[elem] += 1

for i in range(1, 7):
    cnt = count_arr[i]
    print(f"{i} - {cnt}")