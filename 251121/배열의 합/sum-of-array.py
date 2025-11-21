row = 4
list1 = [list(map(int, input().split())) for _ in range(row)]
total = 0

for i in list1:
    total = 0
    for num in i:
        total += num 
    print(total)