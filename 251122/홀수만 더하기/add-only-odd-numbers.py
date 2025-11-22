n = int(input())
sum_val = 0
for i in range(n):
    a = int(input())
    if a % 2 == 1:
        sum_val += a

print(sum_val)