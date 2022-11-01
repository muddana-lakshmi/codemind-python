n,k=map(int,input().split())
l=list(map(int,input().split()))
m=0
for i in range(n):
    c=0
    for j in range(i,n):
        c=c+l[j]
        if c==k:
            m+=1
print(m)