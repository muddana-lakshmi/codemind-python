n=int(input())
s=1
while(n):
  d=n%10
  n=n//10
  if(d>s):
    s=d
print(s)