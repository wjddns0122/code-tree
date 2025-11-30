a, b, c, d = map(int, input().split())
ellapsed_time = 0

# Please write your code here.
while True:
    if a == c and b == d:
        break

    b += 1
    ellapsed_time += 1

    if b == 60:
        b = 0
        a += 1
        
print(ellapsed_time)