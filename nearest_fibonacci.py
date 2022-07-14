n=int(input())
a=1
b=2
d=[]
c=0
d.append(a)
d.append(b)
while (c<(n*n)):
    c=a+b
    a=b
    b=c
    d.append(c)
min=9999
sem=9999
for i in d:
    if i<=n:
        if (n-i)<min:
            min=(n-i)
            x=i
    if i>n:
        if (i-n)<sem:
            sem=(i-n)
            y=i
if min<sem:
    print(x)
elif sem<min:
    print(y)
elif min==sem:
    print(x,y,end=' ')