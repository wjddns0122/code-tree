a, b, c = list(map(int, input().split()))

if a <= b <= c:
    print(a)
if b <= a <= c:
    print(b)
if c <= b <= a:
    print(c)