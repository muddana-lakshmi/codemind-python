n=int(input())
sq=n*n
s=0
while(sq):
  d=sq%10
  sq=sq//10
  s=s+d
if s==n:
    print("Neon Number")
else:
    print("Not Neon Number")