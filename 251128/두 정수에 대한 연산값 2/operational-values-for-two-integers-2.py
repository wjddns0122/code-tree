a, b = map(int, input().split())

# Please write your code here.
def add(a, b):
    if a > b:
        a, b = 2 * a, b + 10
    else:
        b, a = 2 * b, a + 10
    return a, b

print(*add(a, b))