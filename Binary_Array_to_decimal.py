n=int(input())
l=list(map(int,input().split()))
sum=0
k=0
for i in range(len(l)-1,-1,-1):
    sum=sum+(l[i]*(2**k))
    k+=1
print(sum)