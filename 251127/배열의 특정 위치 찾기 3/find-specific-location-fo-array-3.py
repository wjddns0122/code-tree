arr = list(map(int, input().split()))
a = []

for num in arr:
    if num == 0:
        break
    a.append(num)

result = a[-1] + a[-2] + a[-3]
print(result)