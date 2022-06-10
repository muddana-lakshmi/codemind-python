n=input()
n=n.split()
min=100
x=0
for i in n:
    c=0
    k=list(i)
    for j in k:
        if j in 'AEIOUaeiou':
            c+=1
    if c<min:
        min=c
for i in n:
    c=0
    k=list(i)
    for j in k:
        if j in 'AEIOUaeiou':
            c+=1
    if c==min:
        x+=1
print(x)
    