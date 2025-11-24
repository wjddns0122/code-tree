n = int(input())

for i in range(n): 
    for j in range(i): 
        print(' ',end=' ')
    for j in range((2*n)-(2*i)-1): 
        print('*',end=' ') 
    print() 

for i in range(n-1):  # n-1로 수정하여 반복이 0부터 n-2까지만 수행되도록 한다.
    for j in range(n-i-2): 
        print(' ',end=' ') 
    for j in range(3+(2*i)): 
        print('*',end=' ') 
    print()