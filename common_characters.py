a=input()
b=input()
a=a.lower()
b=b.lower()
l=[]
for i in a:
    if i in b:
        if i!=' ':
            l.append(i)
l=set(l)
l=list(l)
l.sort()
if len(l)==0:
    print(-1)
else:
    print(''.join(l))