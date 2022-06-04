n=int(input())
l=list(map(int,input().split()))
k=[]
for i in l:
    k.append(i*i)
j=sorted(k)
for t in j:
    print(t,end=' ')
    