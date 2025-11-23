n = int(input())
sum_val = 1

for i in range(1, n + 1):
    sum_val *= i
    if sum_val >= n:
        print(i)
        break