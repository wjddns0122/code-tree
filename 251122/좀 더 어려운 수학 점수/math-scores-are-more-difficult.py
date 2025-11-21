math_a, eng_a = list(map(int, input().split()))
math_b, eng_b = list(map(int, input().split()))

if math_a > math_b:
    print('A')

elif math_a == math_b:
    if eng_a > eng_b:
        print('A')
    else:
        print('B')
    
else:
    print('B')