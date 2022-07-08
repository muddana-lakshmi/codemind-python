n=int(input())
l=list(map(int,input().split()))
l=set(l)
l=list(l)
x=0
for i in l:
    if l.count(i)==1:
            x+=i
#print(l)
print(x)