n=int(input())
a=0
b=0
c=0
k=0
e=0
f=0
g=0
h=0
i=0
while n:
    d=n%10
    n=n//10
    if d==1:
        a+=1
    elif d==2:
        b+=1
    elif d==3:
        c+=1
    elif d==4:
        k+=1
    elif d==5:
        e+=1
    elif d==6:
        f+=1
    elif d==7:
        g+=1
    elif d==8:
        h+=1
    elif d==9:
        i+=1
if a>1 or b>1 or c>1 or k>1 or e>1 or f>1 or g>1 or h>1 or i>1:
    print("Not Unique Number")
else:
    print('Unique Number')
    