n=int(input())
rev=0
s=0
q=0
for i in range(n+1,2*n):
    k=i
    rev=0
    while(i!=0):
        d=i%10
        i=i//10
        rev=rev*10+d
    if k==rev:
        s=k
        break
for i in range(n-1,-1,-1):
    k=i
    rev=0
    while(i!=0):
        d=i%10
        i=i//10
        rev=rev*10+d
    if k==rev:
        q=k
        break
if abs(n-s)<abs(n-q):
    print(s)
elif abs(n-q)<abs(n-s):
    print(q)
else:
    print(q,s,end=' ')