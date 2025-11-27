arr = list(map(int, input().split()))
cnt = 0
a = []

for num in arr:
    if num == 0:
        break
    elif num % 2 == 0:
        cnt += 1
        a.append(num)

sum_val = sum(a)
    
print(cnt, sum_val)