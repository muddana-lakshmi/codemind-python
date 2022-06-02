import math
n=int(input())
l=list(map(int,input().split()))
sum=0
for i in l:
    k=int(math.sqrt(i))
    if k*k==i:
        sum=sum+i
print(sum)
    