a, b, c = list(map(int, input().split()))

if a > b:
    if a > c:
        if b > c:
            print(b)
        else:
            print(c)

if b > c:
    if b > a:
        if a > c:
            print(a)
        else:
            print(c)

if c > a:
    if c > b:
        if b > a:
            print(b)
        else:
            print(a)
