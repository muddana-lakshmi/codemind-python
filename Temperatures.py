n=int(input())
l=list(map(int,input().split()))
k=0
for i in range(len(l)):
    c=0
    k=0
    for j in range(i,len(l)):
        if l[j]>l[i]:
            c=j
            k+=1
            break
    if(k==0):
        print(0,end=' ')
    else:
        print(c-i,end=' ')