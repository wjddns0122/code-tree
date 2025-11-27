n = int(input())
arr = list(map(int, input().split()))

arr1 = [num ** 2 for num in arr]
for num in arr1:
    print(num, end=" ")