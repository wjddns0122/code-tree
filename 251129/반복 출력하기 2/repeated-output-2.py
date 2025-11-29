n = int(input())

# Please write your code here.
def n_print(n):
    if n == 0:
        return

    print("HelloWorld")
    n_print(n - 1)

n_print(n)