n = int(input())

for i in range(1, n + 1):
    for j in range(n - i, 0, -1):
        print(" ", end="")
    for j in range(2 * i - 1):
        print("*", end="")
    print()

for i in range(n - 1, 0, -1):
    # 왼쪽 공백
    for j in range(n - i):
        print(" ", end="")
    # 별
    for j in range(2 * i - 1):
        print("*", end="")
    print()