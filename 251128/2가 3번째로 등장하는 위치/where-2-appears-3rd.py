n = int(input())
arr = list(map(int, input().split()))
cnt1 = 0
cnt2 = 1
for num in arr:
    if num == 2:
        cnt1 += 1
    if cnt1 == 3:
        break
    cnt2 += 1

print(cnt2)