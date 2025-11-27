n = int(input())
cnt = 0

for _ in range(n):
    arr = list(map(int, input().split()))
    result = sum(arr)
    if result // 4 >= 60:
        print("pass")
        cnt += 1
    else:
        print("fail")

print(cnt)