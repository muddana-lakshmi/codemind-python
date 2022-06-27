a,b=map(int,input().split())
l=list(map(int,input().split()))
k=list(map(int,input().split()))
l=set(l)
k=set(k)
g=[]
for i in l:
    if i not in k:
        g.append(i)
for i in k:
    if i not in l:
        g.append(i)
print(len(g))