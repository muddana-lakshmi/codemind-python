a=input()
b=input()
a=a.split()
b=b.split()
r=[]
s=[]
x=0
for i in a:
    c=0
    for k in a:
        if i==k:
            c+=1
    if c==1:
        r.append(i)
for i in b:
    c=0
    for k in b:
        if i==k:
            c+=1
    if c==1:
        s.append(i)
for j in r:
    if j in s:
        x+=1
print(x)