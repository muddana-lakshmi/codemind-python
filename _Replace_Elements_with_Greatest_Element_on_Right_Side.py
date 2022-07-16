n=int(input())
l=list(map(int,input().split()))
r=[]
for i in range(len(l)):
    t=l
    g=[]
    for j in range(len(t)):
        if j>i:
            g.append(t[j])
    if g!=[]:
        r.append(max(g))
r.append(-1)
print(*r)