a,b=map(int,input().split(':'))
x=(a+b/60)*30
y=b*6
if abs(x-y)<360-(abs(x-y)):
    print(abs(x-y))
else:
    print(360-(abs(x-y)))