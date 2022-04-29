n=int(input())
sq=n*n
re=0
rev=0
while(n):
   d=n%10
   n=n//10
   re=re*10+d
s=re*re
while(s):
   d=s%10
   s=s//10
   rev=rev*10+d
if (sq==rev):
    print("True")
else:
    print("False")