n,a=map(int,input().split())
r=[]
while n!=0:
    d=n%10
    n=n//10
    r.append(d)
k=[]
z=0
for i in r:
    if z<a:
        k.append(i)
        z+=1
r.reverse()
c=0
h=[]
for i in r:
    if c<a:
        h.append(i)
        c+=1
k.reverse()
t='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'
x=''
for i in h:
    i=str(i)
    t=t+i
for i in k:
    i=str(i)
    x=x+i
t=int(t)
x=int(x)
print(abs(t-x))   