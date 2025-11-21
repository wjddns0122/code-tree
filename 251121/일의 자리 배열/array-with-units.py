arr = list(map(int, input().split()))

for i in range(8):
    if (arr[i] + arr[i + 1]) < 10:
        arr.append(arr[i] + arr[i + 1])
    else:
        arr.append(arr[i] + arr[i + 1] - 10)

for x in arr:
    print(x, end=' ')