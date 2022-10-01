n=int(input())
l=list(map(int,input().split()))
k=max(l)
f=[]
for i in range(k*k):
    if i not in l:
        f.append(i)
if(f[0]!=0):
    print(f[0])
else:
    print(f[1])