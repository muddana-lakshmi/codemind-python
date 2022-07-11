n=int(input())
l=list(map(int,input().split()))
k=int(input())
m=l.index(k)
s=0
for i in range(len(l)):
    if i<=m:
        s+=l[i]
    else:
        break
print(s)
        
    
    