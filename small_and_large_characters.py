s=input()
r=list(s.split(' '))
for i in r:
    min=999
    max=0
    k=list(i)
    for j in k:
        if ord(j)<min:
            min=ord(j)
        if ord(j)>max:
            max=ord(j)
    print(chr(min),chr(max),end=' ')
        