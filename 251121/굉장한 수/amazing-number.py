n = int(input())

if n % 2 == 1 and n % 3 == 0:
    print("true")
elif n % 2 == 0 and n % 5 == 0:
    print("true")
else:
    print("false")