row = 4
list1 = [list(map(int, input().split())) for _ in range(row)]
cnt = 0

for i in list1:
    for num in i:
        cnt = list1[0][0] + list1[1][0] + list1[1][1] + list1[2][0] + list1[2][1] + list1[2][2] + list1[3][0] + list1[3][1] + list1[3][2] + list1[3][3]

print(cnt)