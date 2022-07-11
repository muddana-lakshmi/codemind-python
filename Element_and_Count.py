n=int(input())
l=list(map(int,input().split()))
r=[]
for i in l:
    if i not in r:
        r.append(i)
for i in r:
    print(i,l.count(i),end=' ')
    