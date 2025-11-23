ag_av = 0 
cnt = 0

while True:
    age = int(input())

    ag_av += age
    cnt += 1
    if age >= 30 or age <= 19:
        ag_av = ag_av - age
        cnt = cnt - 1
        print(f"{ag_av / cnt:.2f}")
        break