a,b=map(str,input().split())
a=list(a)
b=list(b)
c=0
for i in a:
    if i!=' ':
        if i in b:
            b.remove(i)
        else:
            c+=1
if c>0:
    print("False")
else:
    print("True")