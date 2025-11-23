n = int(input())
has_com = False

for i in range(2, n):
    if n % i == 0:
        has_com = True

if has_com == True:
    print("C")
else:
    print("P")