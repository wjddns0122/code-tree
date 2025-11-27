n = int(input())

for _ in range(n):
    a, b = list(map(int, input().split()))
    sum_val = 1
    for i in range(a, b + 1):
        sum_val *= i

    print(sum_val)