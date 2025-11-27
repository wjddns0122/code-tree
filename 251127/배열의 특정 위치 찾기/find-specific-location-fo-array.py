arr = list(map(int, input().split()))
a = []

result1 = sum(arr[1:len(arr) + 1:2])

for num in arr:
    if num % 3 == 0:
        a.append(num)

result2 = sum(a) / len(a)

print(f"{result1} {result2:.1f}")