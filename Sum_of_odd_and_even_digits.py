n=int(input())
l=list(map(int,input().split()))
sum=0
s=0
for i in range(len(l)):
    if i%2==0:
        sum=sum+l[i]
    else:
        s=s+l[i]
k=s-sum
if k==0:
    print("YES")
else:
    print("NO")
