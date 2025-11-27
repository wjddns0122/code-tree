n = int(input())
arr = list(map(int, input().split()))
a = []

for num in arr:
    if num % 2 == 0:
        a.append(num)

result = a[::-1]
for nums in result:
    print(nums, end=" ")