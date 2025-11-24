n = int(input())

# 첫 줄: 별 2*n개
for j in range(2 * n):
    print("*", end='')
print()

# 두 번째 줄부터 n번째 줄까지
for i in range(1, n):
    # 왼쪽 별: n - i 개
    for j in range(n - i):
        print("*", end='')

    # 가운데 공백: 2 * i 개
    for j in range(2 * i):
        print(" ", end='')

    # 오른쪽 별: n - i 개
    for j in range(n - i):
        print("*", end='')

    print()
