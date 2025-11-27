arr = list(map(int, input().split()))
cnt = 0
a = []

for num in arr:
    if num == 0:
        break
    a.append(num)
    cnt += 1

sum_val = sum(a)
avg = sum_val / cnt
print(f"{sum_val} {avg:.1f}")