n = int(input())

# Please write your code here.
def factorial_recursive(n):
    if n <= 1:
        return 1
    
    # n! = n * (n - 1)!
    return n * factorial_recursive(n - 1)

print(factorial_recursive(n))