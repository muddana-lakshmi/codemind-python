
n1=int(input())
n2=int(input())
k=0
for i in range(n1+n2+1,10**10):
    c=0
    for j in range(1,i+1):
        if i%j==0:
            c+=1
    if c==2:
        k=i
        #print(k)
        break
#print(n1+n2)
print(k-(n1+n2))