n=int(input())
l=[]
for i in range(0,n):
    a=int(input())
    l.append(a)
k=int(input())
sum=0
for j in l:
    if j <=k:
        sum=sum+1
    else:
        sum=sum+2
print(sum)