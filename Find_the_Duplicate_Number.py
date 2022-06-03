n=int(input())
l=list(map(int,input().split()))
c=0
for i in l:
    c=0
    for j in l:
        if i==j:
            c+=1
    if c>1:
        print(i)
        break