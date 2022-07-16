s=input()
n=''
c=0
for i in s:
    if i not in n:
        if i in 'AEIOUaeiou':
            n=n+i
            c+=1
if c==0:
    print(-1)
else:
    for i in n:
        print(i,end=' ')
