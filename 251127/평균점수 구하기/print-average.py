arr = list(map(float, input().split()))

sum_val = sum(arr)
avg = sum_val / len(arr)

print(f"{avg:.1f}")