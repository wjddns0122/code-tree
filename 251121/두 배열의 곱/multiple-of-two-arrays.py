list1 = [
    list(map(int, input().split()))
    for _ in range(3)
]

_ = input()

list2 = [
    list(map(int, input().split()))
    for _ in range(3)
]

for i in range(3):
    for j in range(3):
        print(list1[i][j] * list2[i][j], end=" ")
    print()