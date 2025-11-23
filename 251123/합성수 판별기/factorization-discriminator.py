n = int(input())

is_true = False
for i in range(2, n):
    if n % i == 0:
        is_true = True

if is_true == True:
    print("C")
else:
    print("N")