n = int(input())
arr = [1,n]

for i in range(1,10):
    if arr[i] >= 100 :
        break
    else:
        arr.append(arr[-1]+arr[-2])
print(*arr)
