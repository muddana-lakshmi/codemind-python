n=int(input())
a=[]
i=0
while(n!=0):
    d=n%10
    n=n//10
    a.append(d)
    i+=1
#a.reverse()
for j in range(len(a)-1,-1,-1):
    if a[j]==6:
        a[j]=9
        break
for j in range(len(a)-1,-1,-1):
    print(a[j],end='')