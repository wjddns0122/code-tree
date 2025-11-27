arr = list(map(int, input().split()))
a = []

for num in arr:
    if num % 3 == 0:
        break
    a.append(num)

print(a[-1])