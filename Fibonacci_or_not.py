n=int(input())
a=0
b=1
c=0
for i in range(1,n+1):
    c=a+b
    if c==n:
        print('True')
        break
    elif c>n:
        print('False')
        break
    a=b
    b=c