a,b=map(int,input().split())
l=list(map(int,input().split()))
x=0
for i in l:
    i=abs(i)
    i=str(i)
    if len(i)==b:
        x+=1
print(x)