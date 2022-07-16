s=input()
l=list(s.split(' '))
k=len(l)
g=l[k-1]
min=999
for i in g:
    if ord(i)<min:
        min=ord(i)
if chr(min+32) in g:
    print(chr(min+32))
else:
    print(chr(min))
