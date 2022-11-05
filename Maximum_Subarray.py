n=int(input())
l=list(map(int,input().split()))
s=0
m=[]
for i in range(n):
    m.append(l[i])
for i in range(n):
    c=0
    for j in range(i,n):
        c=c+l[j]
        m.append(c)
print(max(m))
        