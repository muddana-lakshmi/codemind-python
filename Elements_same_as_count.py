n=int(input())
l=list(map(int,input().split()))
r=[]
x=0
for i in l:
    if i==(l.count(i)):
        if i not in r:
            r.append(i)
            x+=1
if x==0:
    print(-1)
else:
    print(*r)