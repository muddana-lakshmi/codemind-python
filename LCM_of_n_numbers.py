n=int(input())
l=list(map(int,input().split()))
c=0
k=1
while(c<=1):
    x=0
    for i in range(0,n):
        if(k%l[i]!=0):
            x+=1
    if x==0:
        c+=1
    k+=1
print((k-1)//2)