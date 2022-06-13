n=int(input())
l=list(map(int,input().split()))
res=0
m=9999
for i in l:
    if m>i:
        m=i
for j in range(m,0,-1):
    res=0
    for k in l:
        if k%j!=0:
            res=1
            break
    if res==0:
        print(j)
        break
    