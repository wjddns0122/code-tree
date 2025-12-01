x,y=0,0

#북동남서 순
dx,dy=[0,1,0,-1],[1,0,-1,0]

n=int(input())
for _ in range(n):
    d_str,dist=tuple(input().split())
    dist=int(dist)

#방향정보 숫자화
    if d_str=='N':
        d_num=0

    elif d_str=='E':
        d_num=1

    elif d_str=='S':
        d_num=2

    else:
        d_num=3

    x,y=x+dist*dx[d_num],y+dist*dy[d_num]

print(x,y)



