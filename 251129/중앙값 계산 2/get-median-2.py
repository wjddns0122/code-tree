n = int(input())
arr = list(map(int, input().split()))#입력 받은 수를 저장하는 배열 
temp = []
for idx, num in enumerate(arr, start=1):
    temp.append(num)
    if idx%2!=0:#인덱스가 홀수 일때, 해당 인덱스 까지 입력 받은 수들을 정렬하여 중앙값을 출럭할 것
        temp.sort()
        print(temp[len(temp)//2], end=" ")
