n=int(input())
l=list(map(int,input().split()))
s=0
for i in range(len(l)):
    if l[i]%2==1:
        s=s+l[i]
print(s)