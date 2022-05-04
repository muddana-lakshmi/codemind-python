n=int(input())
c=0
for i in range(1,n+1):
    if n==i*(i+1):
        c+=1
if c>0:
    print('YES')
else:
    print('NO')
        