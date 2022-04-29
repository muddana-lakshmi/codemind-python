n=int(input())
s=0
m=1
a=0
temp=n
while(n):
  d=n%10
  n=n//10
  m=m*d
while(temp):
  d=temp%10
  temp=temp//10
  s=s+d
if s==m:
  print("Spy Number")
else:
    print("Not Spy Number")
