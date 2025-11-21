a, b = list(map(int, input().split()))

if a < b:
    print(1, 0)
elif a > b:
    print(0, 0)
else:
    print(0, 1)