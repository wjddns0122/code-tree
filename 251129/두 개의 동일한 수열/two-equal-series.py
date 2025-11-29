n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
isTrue = False
# Please write your code here.
A.sort()
B.sort()
for i in range(n):
    if A[i] == B[i]:
        isTrue = True 
    else:
        isTrue = False 

if isTrue == True:
    print("Yes")
else:
    print("No")