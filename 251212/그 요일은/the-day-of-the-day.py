m1, d1, m2, d2 = map(int, input().split())
A = input()

#                  1   2  3   4   5   6   7   8   9   10  11  12
num_of_days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

def totalDay(m,d):
    num = 0
    for i in range(1, m):
        num += num_of_days[i]
    num+=d
    return num

start_day = (totalDay(m1, d1) - 1) % 7
elapsed_day = totalDay(m2,d2) - totalDay(m1,d1) + 1

count = 0
for i in range(elapsed_day):
    index = (start_day + i) % 7
    day = week[index]
    if day == A:
        count += 1

print(count)
