n, a = list(map(int, input().split()))


while n >= 1:
    if n % a == 0:
        print(1)
    else:
        print(0)
    n -= 1    