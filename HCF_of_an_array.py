n=int(input())
l=list(map(int,input().split()))
k=max(l)
s=1
for i in range(1,k+1):
    c=0
    for j in l:
        if j%i==0:
            c+=1
    if c==len(l):
        s=i
print(s)