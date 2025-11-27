a,b = map(int,input().split())
arr = [0]*10
sum = 0

while True :
    if a<=1 :
        break
    arr[a%b]+=1
    a //= b 

for i in arr :
    sum += i**2

print(sum)
