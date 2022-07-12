n=int(input())
r=[]
t=[]
for i in range(n+1):
    if (2**i)<=n:
        r.append(n-(2**i))
    else:
        t.append((2**i)-n)
if min(r)<min(t):
    print(min(r))
else:
    print(min(t))
