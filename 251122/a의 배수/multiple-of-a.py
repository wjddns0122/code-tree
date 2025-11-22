n, a = list(map(int, input().split()))

if n % a == 0:
    print(1)
else:
    print(0)

while n > 1:
    n -= 1    
    if n % a == 0:
        print(1)
    else:
        print(0)