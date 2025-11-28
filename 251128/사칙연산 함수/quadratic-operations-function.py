a, o, c = input().split()
a = int(a)
c = int(c)

# Please write your code here.
def calculate(a, o, c):
    if o == "+":
        return print(f"{a} + {c} = {a + c}")
    if o == "-":
        return print(f"{a} - {c} = {a - c}") 
    if o == "/":
        return print(f"{a} / {c} = {a // c}")
    if o == "*":
        return print(f"{a} * {c} = {a * c}")
    else:
        return print(False)
    
calculate(a, o, c)