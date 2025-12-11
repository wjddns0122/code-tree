m1, d1, m2, d2 = map(int, input().split())

# Please write your code here.
days = [0,31,28,31,30,31,30,31,31,30,31,30,31]
sum_days = [0]
for i in range(12):
    sum_days.append(sum_days[i]+days[i+1])

days_1 = sum_days[m1-1] + d1
days_2 = sum_days[m2-1] + d2

day = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]

dif = (days_2 - days_1) % 7
print(day[dif])
