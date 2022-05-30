n=int(input())
k=n
l=1
for i in range(1,n+1):
    l=i
    for j in range(1,k+1):
        print(l,end=' ')
        l+=1
    k-=1
    print()