A = input()
# Please write your code here.
def sd(A):
    cnt = 0
    for i in range(len(A)):
        if A[i] == A[i + 1]:
            cnt += 1
            if cnt >= 2:
                break
                return False
        else:
            return True

if sd(A) == True:
    print("Yes")
else:
    print("No")