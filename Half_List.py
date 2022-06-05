n=int(input())
l=list(map(int,input().split()))
k=[]
b=[]
for i in range(len(l)):
    if i<n//2:
        k.append(l[i])
for j in range(len(l)-1,-1,-1):
    if j>=n//2:
        b.append(l[j])
print(*(b+k))
    