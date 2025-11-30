n = int(input())

class Weather:
    def __init__(self, date, day, weath):
        self.date = date
        self.day = day
        self.weath = weath

w = []

for _ in range(n):
    date, day, we = input().split()
    if we == "Rain":
        w.append(Weather(date, day, we))

w = sorted(w, key=lambda x: x.date)

print(w[0].date, w[0].day, w[0].weath, sep=" ")