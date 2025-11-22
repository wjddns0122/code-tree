a, b = list(map(int, input().split()))
sum_val = 0

for i in range(a, b + 1):
    if i % 2 == 0:
        sum_val += i

print(sum_val)