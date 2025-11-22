sum_val = 0
cnt = 0

for i in range(10):
    n = int(input())
    if n >= 0 and n <= 200:
        sum_val += n
        cnt += 1

print(f"{sum_val} {sum_val / cnt:.1f}")