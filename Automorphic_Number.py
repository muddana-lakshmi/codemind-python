n=int(input())
import math
temp=n
sq=n*n
c=0
s=0
while(n!=0):
    d=n%10
    n=n//10
    c+=1
while(sq!=0):
    p=int(math.pow(10,c))
    l=sq%p
    sq=sq//10
    if(l==temp):
        print("Automorphic Number")
        s+=1
        break
if(s==0):
    print("Not an Automorphic Number")