n = int(input())

for i in range(1, n):
    print("*" * i)
    print()

for i in range(n + 1):
    for j in range(n - i):
        print("*", end="")
    print()
    print()