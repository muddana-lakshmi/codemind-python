n=int(input())
l=list(map(int,input().split()))
r=[]
for i in l:
    if i==(l.count(i)):
        if i not in r:
            r.append(i)
print(len(r))