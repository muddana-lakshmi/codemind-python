n=int(input())
c=0
k=0
while n>0:
    d=n%10
    n=n//10
    if d%2==0:
        c+=1
    else:
        k+=1
if c>0 and k>0:
    print('Mixed')
elif c==0 and k>0:
    print('Odd')
elif c>0 and k==0:
    print("Even")