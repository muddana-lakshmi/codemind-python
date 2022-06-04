n=int(input())
l=list(map(int,input().split()))
c=0
k=0
for i in l:
    c=0
    while i!=0:
        d=i%10
        i=i//10
        c+=1
    if c%2==0:
        k+=1
print(k)
    