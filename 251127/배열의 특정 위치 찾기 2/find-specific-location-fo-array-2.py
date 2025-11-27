arr = list(map(int, input().split()))

even = sum(arr[::2])
odd = sum(arr[1::2])
    
if even > odd:
    print(even - odd)
else:
    print(odd - even)