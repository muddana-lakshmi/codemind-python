l=list(map(int,input().split()))
#print(l)
k=max(l)
for i in l:
    if i==k:
        l.remove(i)
        break
y=max(l)
print((k-1)*(y-1))