n = int(input())

# Please write your code here.
def recursive(n):
    if n < 10:
        return n ** 2

    return recursive(n // 10) + (n % 10) ** 2

print(recursive(n))