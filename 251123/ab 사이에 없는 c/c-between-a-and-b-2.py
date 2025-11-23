a, b, c = list(map(int, input().split()))

has_common = False
for i in range(a, b + 1):
    if i % c == 0:
        has_common = True

if has_common == True:
    print("NO")
else:
    print("YES")