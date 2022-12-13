n=int(input())
l=list(map(int,input().split()))
c=0
#print(n)
for i in range(n):
    if i<n-2:
        if l[i]!=l[i+2]-l[i+1]:
            c+=1
for i in range(n-1,-1,-1):
    if i>=2:
        if l[i]!=l[i-1]+l[i-2]:
            c+=1
for i in range(n//2-1,-1,-1):
    if i>=n//2-2:
        if l[i]!=l[i-1]+l[i-2]:
            c+=1
if c>0:
    print("no")
else:
    print("yes")
        