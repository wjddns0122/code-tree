M, D = map(int, input().split())

# Please write your code here.
def is_thiryone():
    if M == 1 or M == 3 or M == 5 or M == 7 or M == 8 or M == 10 or M == 12:
        if D <= 31:
            print("Yes")
        else:
            print("No")
    elif M == 4 or M == 6 or M == 9 or M == 11:
        if D <= 30:
            print("Yes")
        else:
            print("No")
    else:
        if D <= 28:
            print("Yes")
        else:
            print("No")

is_thiryone()