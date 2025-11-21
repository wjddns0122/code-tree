a, b, c = list(map(int, input().split()))

if a == c or a == b:
    print(1, end=" ")
else:
    print(0, end=" ")

if a == b == c:
    print(1)
else:
    print(0)