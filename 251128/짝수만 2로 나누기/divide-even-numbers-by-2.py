n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
for num in arr:
    if num % 2 == 0:
        num //= 2
    print(num, end=" ")