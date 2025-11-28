n = int(input())

# Please write your code here.
def add(n):
    result = 0
    for i in range(1, n + 1):
        result += i
    result //= 10
    return print(result)

add(n)