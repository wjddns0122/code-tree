n = int(input())

# Please write your code here.
def is_magic_number(n):
    result = 0
    result = n // 10
    result1 = n % 10
    result2 = result + result1
    if n % 2 == 0 and result2 % 5 == 0:
        print("Yes")
    else:
        print("No")

is_magic_number(n)