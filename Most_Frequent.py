n=int(input())
l=list(map(int,input().split()))
r=[]
for i in l:
    r.append(l.count(i))
k=max(r)
u=[]
for i in l:
    if l.count(i)==k:
        u.append(i)
u=set(u)
u=list(u)
if len(u)<=1:
    print(*u)
else:
    print(min(u))