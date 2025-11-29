n = int(input())

# Please write your code here.
def recursive(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    return n // 3 + recursive(n - 1)

print(recursive(n))