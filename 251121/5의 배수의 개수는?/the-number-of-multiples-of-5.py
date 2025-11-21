row = 4 
list1 = [list(map(int, input().split())) for _ in range(row)]
cnt = 0

for i in list1:
    for num in i:
        if num % 5 == 0:
            cnt += 1
        
print(cnt)