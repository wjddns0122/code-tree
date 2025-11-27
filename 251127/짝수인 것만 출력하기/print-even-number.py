n = int(input())
arr = list(map(int, input().split()))
a = []

for num in arr:
    if num % 2 == 0:
        a.append(num)
    else:
        continue

for x in a:
    print(x, end=" ")