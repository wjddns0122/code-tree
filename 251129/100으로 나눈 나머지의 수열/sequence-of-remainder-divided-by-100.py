N = int(input())

def recursion(n):
    if n == 1:
        return 2
    if n == 2:
        return 4
    # n >= 3 인 경우
    return recursion(n - 1) * recursion(n - 2) % 100

print(recursion(N))
