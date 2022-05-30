k=65
n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        print(chr(k),end=' ')
    k+=1
    print()