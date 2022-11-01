n=int(input())
l=list(map(int,input().split()))
k=list(map(int,input().split()))
j=sum(l)-sum(k)
if j<0:
    print(-(j))
else:
    print(0)