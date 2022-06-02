n=int(input())
d=2
a=0
b=1
print(a,end=' ')
print(b,end=' ')
while d<n:
    c=a+b
    print(c,end=' ')
    d+=1
    a=b
    b=c
    
    