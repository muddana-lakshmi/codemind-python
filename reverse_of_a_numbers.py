n=int(input())
s=0
while(n):
  d=n%10
  n=n//10
  s=s*10+d
print(s)