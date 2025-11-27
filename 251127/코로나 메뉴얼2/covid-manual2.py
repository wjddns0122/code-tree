arr=[0]*4
for _ in range(3):
    a, b = list(map(str, input().split()))
    #print(a, b)
    if a=='Y':
        if int(b)>=37:
            arr[0]+=1
        else: arr[2]+=1
    elif a=='N':
        if int(b)>=37:
            arr[1]+=1
        else:
            arr[3]+=1
for elem in arr:
    print(elem, end=" ")
if arr[0]>=2:
    print('E')
