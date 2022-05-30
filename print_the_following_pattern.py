n=int(input())
k=65+n-1
l=n
for i in range(1,n+1):
    for j in range(1,l+1):
        print(chr(k),end=' ')
    k-=1
    l-=1
    print()