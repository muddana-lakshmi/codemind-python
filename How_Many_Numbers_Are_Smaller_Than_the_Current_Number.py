n=int(input())
l=list(map(int,input().split()))
c=0
for i in l:
    c=0
    for j in l:
        if j<i:
            c+=1
    print(c,end=' ')
    