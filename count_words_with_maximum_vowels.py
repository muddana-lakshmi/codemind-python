n=input()
n=n.split()
max=0
x=0
for i in n:
    c=0
    k=list(i)
    for j in k:
        if j in 'AEIOUaeiou':
            c+=1
    if c>max:
        max=c
for i in n:
    c=0
    k=list(i)
    for j in k:
        if j in 'AEIOUaeiou':
            c+=1
    if c==max:
        x+=1
print(x)
    