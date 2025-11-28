y = int(input())

def is_yoonyun(n):
    if n % 400 == 0:
        print("true")
    elif n % 100 == 0:
        print("false")
    elif n % 4 == 0:
        print("true")
    else:
        print("false")

is_yoonyun(y)
