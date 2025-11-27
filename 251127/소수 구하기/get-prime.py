n = int(input())
for i in range(1, n + 1):
	if i == 1:
		continue
	isprime = True
	
	for j in range(2, i):
		if i % j == 0:
			isprime = False
	
	if isprime == True:
		print(i, end=" ")