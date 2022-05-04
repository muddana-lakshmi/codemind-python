a=int(input())
b=int(input())
s=0
l=0
for i in range(1,a):
    if a%i==0:
        s=s+i
for i in range(1,b):
    if b%i==0:
        l=l+i
if l==a and s==b:
    print('Amicable')
else:
    print('Not Amicable')