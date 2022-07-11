n=int(input())
l=list(map(int,input().split()))
r=[]
x=0
for i in l:
    c=0
    for j in l:
        if i==j:
            c+=1
    if(i==c):
        r.append(i)
        x+=1
if(x==0):
    print(-1)
else:
    print(min(r),max(r))
        