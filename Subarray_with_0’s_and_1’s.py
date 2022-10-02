n=int(input())
l=list(map(int,input().split()))
k=[]
for i in range(n):
    c=0
    x=0
    for j in range(i,n):
        if l[j]==0:
            c+=1
        if l[j]==1:
            x+=1
        if c==x:
            k.append(i)
            k.append(j)
m=0
for i in range(len(k)):
    if(i%2==0):
        if(k[i+1]-k[i]>m):
            m=k[i+1]-k[i]
if(len(k)==0):
    print(-1)
else:
    for i in range(len(k)):
        if i%2==0:
            if (k[i+1]-k[i]==m):
                print(k[i],k[i+1])
                break
            