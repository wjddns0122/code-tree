n = int(input())

def recursive_factorial(n):
    # 0! = 1, 1! = 1
    if n <= 1:
        return 1
    
    return recursive_factorial(n - 1) + n

print(recursive_factorial(n))
