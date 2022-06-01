n=int(input())
l=list(map(int,input().split()))
c=0
k=0
x=0
s=max(l)
while s:
    d=s%10
    s=s//10
    c+=1
#print(c)
for i in l:
    k=0
    while i:
        d=i%10
        i//=10
        k+=1
    if k==c:
        x+=1
print(x)
    