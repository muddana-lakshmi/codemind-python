n=int(input())
for i in range(1,n+1):
    for j in range(1,n-2+1):
        print(j,end='')
    for j in range(1,n-3+1):
        print(j,end='')
    print()
        