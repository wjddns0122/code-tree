arr = list(map(int, input().split()))
a = []

result1 = sum(arr[1:len(arr) + 1:2])
result2 = sum(arr[2::3]) / len(arr[2::3])


print(f"{result1} {result2:.1f}")