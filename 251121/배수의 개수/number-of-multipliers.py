cnt1=0
cnt2=0
a=[]
for i in range(10):
    a=int(input())
    if(a%3==0):
        cnt1+=1
    if(a%5==0):
        cnt2+=1
print(cnt1,cnt2,end=" ")