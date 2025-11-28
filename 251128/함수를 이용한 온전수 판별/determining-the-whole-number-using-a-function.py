a, b = map(int, input().split())

def count_onjeonsu(a, b):
    cnt = 0
    for i in range(a, b + 1):
        # 온전수가 아닌 조건
        if (i % 2 == 0) or (i % 5 == 0 and i % 10 != 0) or (i % 3 == 0 and i % 9 != 0):
            continue      # 온전수가 아니니까 스킵

        # 여기까지 왔다는 건 온전수라는 뜻
        cnt += 1

    return cnt

print(count_onjeonsu(a, b))
