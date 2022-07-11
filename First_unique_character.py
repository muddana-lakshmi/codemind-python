s=input()
k=''
x=0
for i in s:
    c=0
    for j in s:
        if i==j:
            c+=1
    if c==1:
        k=k+i
        x+=1
if x==0:
    print(-1)
else:
    for i in k:
        print(i)
        break