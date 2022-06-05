l=list(map(int,input().split(',')))
a=[]
x=0
for i in l:
    c=0
    for j in range(1,i+1):
        if i%j==0:
            c=c+j
    #print(c)
    if c in l:
            a.append(i)
            x+=1
if x==0:
    print(-1)
else:
    a=sorted(a)
    print(*a)
            