arr = list(map(int, input().split()))
a = []

for num in arr:
    if num % 3 == 0:
        a.append(num)

result1 = sum(arr[1::2])
result2 = sum(a) / len(a)

print(f"{result1} {result2:.1f}")