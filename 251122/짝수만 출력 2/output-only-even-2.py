b, a = list(map(int, input().split()))
print(b, end=" ")
while b > a:
    b -= 2
    print(b, end=" ")