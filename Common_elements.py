n,m=map(int,input().split())
l=list(map(int,input().split()))
a=list(map(int,input().split()))
r=[]
for i in l:
    if i in a:
        r.append(i)
s=[]
for i in r:
    if i not in s:
        s.append(i)
print(*s)
    
