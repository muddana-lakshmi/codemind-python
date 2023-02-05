n=int(input())
k=1
for i in range(1,n+1):
    for j in range(i,n):
        print(" ",end='')
    for j in range(1,k+1):
        print(i,end='')
    k=k+2
    print()