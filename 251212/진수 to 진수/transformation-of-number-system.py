a, b = list(map(int, input().split()))
n = input()

result1 = int(n, a)

digits = []

while True:
    if result1 < b:
        digits.append(result1)
        break

    digits.append(result1 % b)
    result1 //= b

for digit in digits[::-1]:
    print(digit, end="")