n,m=map(int,input().split())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
x=[]
y=[]
for i in l1:
    if i not in x:
        x.append(i)
for i in l2:
    if i not in y:
        y.append(i)
r=[]
for i in x:
    if (i in x) and (i in y):
        r.append(i)
print(*r)