a, b, c = list(map(int, input().split()))

if a <= b <= c:
    print(a)
elif b <= a <= c:
    print(b)
elif c <= b <= a:
    print(c)