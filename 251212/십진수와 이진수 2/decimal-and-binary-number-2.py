N = input()
arr = list(map(int, str(N)))
# Please write your code here.
num = 0

for i in range(len(arr)):
    num = num * 2 + arr[i]

final_num = num * 17

digits = []

while True:
    if final_num < 2:
        digits.append(final_num)
        break

    digits.append(final_num % 2)
    final_num //= 2

for digit in digits[::-1]:
    print(digit, end="")