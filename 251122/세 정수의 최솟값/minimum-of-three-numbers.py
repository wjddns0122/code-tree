a, b, c = list(map(int, input().split()))

if a <= b <= c and a <= c <= b:
    print(a)
if b <= a <= c and b <= c <= a:
    print(b)
if c <= b <= a and c <= a <= b:
    print(c)