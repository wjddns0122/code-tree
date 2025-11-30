a, b, c = map(int, input().split())
ellapsed_min = 0
# Please write your code here.
while True:
    if a == 11 and b == 11 and c == 11:
        break
    
    if a < 11:
        print(-1)

    ellapsed_min += 1
    c -= 1
    if c == 0:
        b -= 1
        c = 60

    if b == 0:
        a -= 1
        b = 24

print(ellapsed_min)