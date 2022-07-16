s=input()
r=list(s.split(' '))
for i in r:
    k=list(i)
    min=999
    max=0
    for j in k:
        if ord(j)<min:
            min=ord(j)
        if ord(j)>max:
            max=ord(j)
    print(abs(min-max),end=' ')