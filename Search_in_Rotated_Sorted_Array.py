n=int(input())
k=[]
c=0
l=list(map(int,input().split()))
for i in l:
    k.append(i)
a=int(input())
for j in range(0,len(l)):
    if l[j]==a:
        print(j)
        c+=1
if c==0:
    print(-1)
    