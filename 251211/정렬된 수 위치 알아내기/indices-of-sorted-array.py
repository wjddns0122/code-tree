n = int(input())
sequence = list(map(int, input().split()))

# Please write your code here.

l1 = []
for idx, s in enumerate(sequence):
    l1.append([idx, s])

l2 = l1[:]
l1.sort(key = lambda x:x[1])
for i in range(len(l1)):
    l1[i][0] = i + 1    

for i in range(len(l2)):
    print(l2[i][0], end = " ")

