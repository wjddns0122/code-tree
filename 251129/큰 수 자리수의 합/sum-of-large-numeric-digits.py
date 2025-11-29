a, b, c = map(int, input().split())

# Please write your code here.
result = a * b * c 
def digit_sum(result):
    if result < 10:
        return result 
    
    return (result % 10) + digit_sum(result // 10)

print(digit_sum(result))