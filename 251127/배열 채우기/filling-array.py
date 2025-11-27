arr = list(map(int, input().split()))
a = []
b = 0

for num in arr:
    if num == 0:
        break
    a.append(num)
    
result = a[::-1]
for nums in result:
    print(nums, end=" ")