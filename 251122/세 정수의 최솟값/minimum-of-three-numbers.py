a, b, c = list(map(int, input().split()))

if a <= b <= c and a <= c <= b
    print(a)
elif b <= a <= c and b <= c <= a
    print(b)
elif c <= b <= a and c <= a <= b
    print(c)