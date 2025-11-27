a, b = list(map(int, input().split()))

arr = [a, b]
for i in range(2, 10):
    arr.append(arr[i - 1] + 2 * arr[i - 2])

print(*arr)