def prime(n):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c+=1
    if c==2:
        return 1
    else:
        return 0

n=int(input())
c=prime(n)
if prime(n):
    rev=0
    while n:
        d=n%10
        n=n//10
        rev=rev*10+d
    if prime(rev):
        print('circular prime')
    else:
        print("prime but not a circular prime")
else:
    print("not prime")