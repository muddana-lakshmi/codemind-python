n=int(input())
for i in range(1,n+1):
    for j in range(i,n):
        print(" ",end='')
    for j in range(i-1,0,-1):
        print(j,end='')
    print("0",end='')
    for j in range(1,i):
        print(j,end='')
    print()