n = int(input())
x = 0

while n > 1:      # n이 1이 될 때까지 2로 나눈다
    n //= 2
    x += 1

print(x)
