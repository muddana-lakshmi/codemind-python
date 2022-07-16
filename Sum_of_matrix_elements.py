n=int(input())
m=int(input())
sum=0
for i in range(n):
    l=list(map(int,input().split()))
    for i in l:
        sum=sum+i
print(sum)