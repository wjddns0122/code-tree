N = int(input())

# Please write your code here.
def print_flower(N):
    if N == 0:
        return

    print(N, end=" ")
    print_flower(N-1)
    print(N, end=" ")

print_flower(N)