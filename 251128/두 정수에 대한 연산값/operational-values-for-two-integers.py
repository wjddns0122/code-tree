a, b = map(int, input().split())

# Please write your code here.
def swap(a, b):
    if a > b:
        a, b = a + 25, b * 2
    else:
        b, a = b + 25, a * 2
    return a, b

print(*swap(a, b))