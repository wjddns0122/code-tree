gender = int(input())
age = int(input())

if age >= 19:
    if gender == 0:
        print("MAN")
    if gender == 1:
        print("WOMAN")
else:
    if gender == 0:
        print("BOY")
    if gender == 1:
        print("GIRL")