n=int(input())
s=0
sum=0
for i in range(0,n):
    sum=0
    a=int(input())
    l=list(map(int,input().split()))
    s=(a*(a+1))//2
    for j in l:
        sum=sum+j
    print(s-sum)
    #print(s-sum)
        