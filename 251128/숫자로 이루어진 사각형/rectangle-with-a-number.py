n = int(input())

# Please write your code here.  
def star(n):
    cnt = 0
    for i in range(n):
        for j in range(n):
            cnt += 1
            if cnt == 10:
                cnt = 0
                cnt += 1
            print(cnt, end=" ")
        print()

star(n)