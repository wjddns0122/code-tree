a, b, c = list(map(int, input().split()))

has_c = False
for i in range(a, b + 1):
    if i % c == 0:
        has_c = True

if has_c == True:
    print("YES")
else:
    print("NO")