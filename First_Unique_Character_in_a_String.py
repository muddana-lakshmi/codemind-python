a=input()
x=0
z=0
for i in a:
    c=0
    for j in a:
        if i==j:
            c+=1
    if c==1:
        z=a.index(i)
        x+=1
    if x==1:
        break
    else:
        continue
    break
if x==0:
    print("-1")
else:
    print(z)