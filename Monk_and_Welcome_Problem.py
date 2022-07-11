n=int(input())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
l3=[]
for i in range(len(l1)):
    for j in range(len(l2)):
        if i==j:
            k=l1[i]+l2[j]
            l3.append(k)
print(*l3)

            