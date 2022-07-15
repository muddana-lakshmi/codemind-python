def prime(i):
    for j in range(2,int(i**0.5+1)):
        if i%j==0:
            return 0
    else:
        return 1
n=int(input())
k=0
for i in range(n+1,100001):
    k=0
    if prime(i):
        z=i
        while i:
            d=i%10
            i=i//10
            k=k*10+d
        if k==z:
            print(z)
            break