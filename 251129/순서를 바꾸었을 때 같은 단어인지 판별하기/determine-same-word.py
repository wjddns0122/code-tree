word1 = input()
word2 = input()
arr1 = list(word1)
arr2 = list(word2)

# Please write your code here.
arr1.sort()
arr2.sort()

if arr1 == arr2:
    print("Yes")
else:
    print("No")