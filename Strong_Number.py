n=int(input())
s=0
temp=n
while n:
    i=1
    res=1
    d=n%10
    while i<=d:
        res=res*i
        i+=1
    s=s+res
    n=n//10
if s==temp:
    print('The number',temp,'is a strong number')
else:
    print("The number",temp,"is not a strong number")