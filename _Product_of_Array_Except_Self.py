n=int(input())
l=list(map(int,input().split()))
p=1
for i in range(len(l)):
    p=1
    for j in range(len(l)):
        if i!=j:
            p=p*l[j]
    print(p,end=' ')
        