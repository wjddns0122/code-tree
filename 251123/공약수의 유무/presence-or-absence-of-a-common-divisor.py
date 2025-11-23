a, b = list(map(int, input().split()))

has_some = False
for i in range(a, b + 1):
    if 1920 % i == 0 and 2880 % i == 0:
        has_some = True

if has_some == True:
    print(1)
else:
    print(0)