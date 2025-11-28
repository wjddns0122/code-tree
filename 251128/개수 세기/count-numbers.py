n, m = list(map(int, input().split()))
arr = list(map(int, input().split()))
cnt = 0

for num in arr:
    if num == 3:
        cnt += 1
    
print(cnt)