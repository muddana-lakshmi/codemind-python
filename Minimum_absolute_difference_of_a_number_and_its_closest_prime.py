n=int(input())
i=n
while i:
    c=0
    for j in range(1,i+1):
        if i%j==0:
            c+=1
    if c==2:
        d=i
        break
    i+=1
i=n
while i:
    c=0
    for j in range(1,i+1):
        if i%j==0:
            c+=1
    if c==2:
        k=i
        break
    i-=1
f=abs(d-n)
x=abs(n-k)
if f<x:
    print(f)
else:
    print(x)
