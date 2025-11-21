a1, s1 = input().split()
a2, s2 = input().split()
a1 = int(a1)
a2 = int(a2)

if (a1 >= 19 and a2 >= 19) and (s1 == "M" or s2 == "M"):
    print(1)
elif (a1 >= 19 or a2 >= 19) and (s1 == "M" or s2 == "M"):
    print(1)
else:
    print(0)