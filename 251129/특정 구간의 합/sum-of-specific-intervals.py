n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [tuple(map(int, input().split())) for _ in range(m)]


def calculate():
    result = 0
    for elem in queries:
        a = elem[0]; b=elem[1]
        result = sum(arr[a-1:b])
        print(result)
            
calculate()

