n = int(input())


#규칙에 의해 조건에 해당하는 경우 *출력, 아닌경우 공백 출력
for i in range(1, n + 1): 
    for j in range(1, n + 1):  
        if i == 1 or j % 2 == 0  and i <= j:
            print("* ", end = "")
        else : 
            print("  ", end = "")
        
    print()
