n=int(input())
k=int(input())
m=0
for i in range(n,k+1):
    c=0
    for j in range(i,k+1):
        c=c+j
        if c%2==1:
            m+=1
print(m)