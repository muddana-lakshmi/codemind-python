n=int(input())
c=0
x=0
y=0
for i in range(2,n):
    if n%i==0:
        c+=1
if c==0:
    while n>0:
        d=n%10
        n=n//10
        for i in range(2,d):
            if d%i==0:
                x+=1
        if d==1:
            y+=1
if c==0 and x==0 and y==0:
    print('Mega Prime')
else:
    print('Not Mega Prime')