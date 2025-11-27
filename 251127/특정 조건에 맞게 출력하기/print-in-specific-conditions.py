arr = list(map(int, input().split()))
a = []
for num in arr:
    if num == 0:
        break
    if num % 2 == 0:
        a.append(num // 2)
    elif num % 2 == 1:
        a.append(num + 3)

print(*a)