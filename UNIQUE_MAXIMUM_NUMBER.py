n=int(input())
l=list(map(int,input().split()))
c=0
m=0
k=[]
for i in l:
    c=0
    for j in l:
        if i==j:
            c+=1
    if c==1:
        k.append(i)
        m+=1
if m==0:
    print(-1)
else:
    print(max(k))
        
    
