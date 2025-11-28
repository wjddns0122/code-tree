n,m = map(int, input().split())
a = list(map(int, input().split()))

def abc(a, m):

    m_sum = 0
    while m:
        m_sum += a[m-1]
        if m % 2 == 0:
            m //= 2
        else:
            m -= 1
        # print(m)

    return m_sum

result = abc(a,m)
print(result)
