mid, last = list(map(int, input().split()))

if mid >= 90:
    if last >= 95:
        print("100000")
    elif last >= 90:
        print("50000")
    else:
        print("0")