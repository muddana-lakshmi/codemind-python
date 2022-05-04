n=int(input())
j=0
s=0
while s!=1 and s!=4 and s!=7:
    s=0
    while n>0:
        d=n%10
        n=n//10
        s+=(d*d)
    n=s
if s==1:
    print('True')
else:
    print("False")