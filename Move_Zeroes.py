n=int(input())
l=list(map(int,input().split()))
k=[]
m=[]
for i in l:
    if i==0:
        k.append(i)
    else:
        m.append(i)
j=m+k
for s in j:
    print(s,end=' ')
        
    