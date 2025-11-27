arr = input().split()
numbers = []

for i in arr:
    if int(i) >= 10:
        numbers.append(i)

for i in range(100,9,-10):
    cnt = 0
    for j in numbers:
        if (i/10) == (int(j)//10):
            cnt += 1
    print(f'{i} - {cnt}')
