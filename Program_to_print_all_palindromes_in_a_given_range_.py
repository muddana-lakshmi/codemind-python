a=int(input())
b=int(input())
for i in range(a,b+1):
    sum=0
    temp=i
    while i>0:
        d=i%10
        i=i//10
        sum=sum*10+d
    if temp==sum:
        print(temp,end=' ')