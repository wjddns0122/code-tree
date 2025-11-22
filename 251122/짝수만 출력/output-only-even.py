a, b = list(map(int, input().split()))
if a % 2 == 0 and b % 2 == 0:
    print(a, end=" ")
    while a < b:
        a += 2
        print(a, end=" ")