x=int(input())
k=0
if x>0:
    while x:
        d=x%10
        x=x//10
        k=k*10+d
    print(k)
else:
    s=abs(x)
    while s:
        d=s%10
        s=s//10
        k=k*10+d
    print(-k)
    