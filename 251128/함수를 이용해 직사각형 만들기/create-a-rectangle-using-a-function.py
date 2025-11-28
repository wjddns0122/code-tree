n, m = map(int, input().split())

# Please write your code here.

def star(n, m):
    for _ in range(n):
        print("1" * m)

star(n, m)