n = int(input())
num1 = 2 * n + 1
num2 = 1 + n

for i in range(2 * n + 1):
    if i % 2 == 0:
        print("* " * num1, end="")
        print()
    else:
        print("*   " * num2, end="")
        print()
