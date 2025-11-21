arr = [
	list(map(int, input().split()))
	for _ in range(3)
]

for i in range(3):
    for j in range(3):
        arr[i][j] *= 3
	
for row in arr:
	for elem in row:
		print(elem, end=" ")
	print()
