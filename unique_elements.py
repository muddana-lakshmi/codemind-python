n=int(input())
l=list(map(int,input().split()))
r=[]
x=0
for i in l:
    c=0
    for j in l:
        if i==j:
            c+=1
    if(c>=1):
        r.append(i)
w=[]
for i in r:
    if i not in w:
        w.append(i)
print(*w)
        