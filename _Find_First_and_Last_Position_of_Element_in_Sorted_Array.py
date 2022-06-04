n=int(input())
l=list(map(int,input().split()))
a=int(input())
k=0
v=0
c=0
for i in range(len(l)):
    if l[i]==a:
        k=i
        c+=1
        break
for j in range(len(l)-1,-1,-1):
    if l[j]==a:
        v=j
        c+=1
        break
if c==0:
    print("-1 -1")
else:
    print(k,v)
        