n=int(input())
l=list(map(int,input().split()))
a=int(input())
k=max(l)
m=[]
for i in l:
    if a+i>=k:
        m.append("True")
    else:
        m.append("False")
print(*m)
        