n = int(input())

def sum_even(x):
    # 2 + 4 + ... + x  (x는 짝수)
    if x == 0:
        return 0
    return x + sum_even(x - 2)

def sum_odd(x):
    # 1 + 3 + ... + x  (x는 홀수)
    if x == 1:
        return 1
    return x + sum_odd(x - 2)

if n % 2 == 0:          # n이 짝수면 짝수들만 더함
    print(sum_even(n))
else:                   # n이 홀수면 홀수들만 더함
    print(sum_odd(n))
