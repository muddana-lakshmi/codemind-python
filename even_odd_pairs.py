n=int(input())
l=list(map(int,input().split()))
e=[]
o=[]
for i in l:
    if i%2==0:
        e.append(i)
    else:
        o.append(i)
v=[]
if len(o)<len(e):
    for i in range(len(o)):
        v.append(e[i])
        v.append(o[i])
    for i in range(len(o),len(e)):
        v.append(e[i])
    if n%2==1:
        v.append(0)
if len(e)<len(o):
    for i in range(len(e)):
        v.append(e[i])
        v.append(o[i])
    for i in range(len(e),len(o)):
        v.append(o[i])
    if n%2==1:
        v.append(0)
if len(e)==len(o):
    for i in range(len(e)):
        v.append(e[i])
        v.append(o[i])
print(*v)