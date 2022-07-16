s=input()
r=list(s.split(' '))
min=999
max=0
#print(r)
#print(r[0])
#print(r[len(r)-1])
r[0]=list(r[0])
r[len(r)-1]=list(r[len(r)-1])
for i in r[0]:
    if ord(i)<min:
        min=ord(i)
for i in r[len(r)-1]:
    if ord(i)>max:
        max=ord(i)
print(chr(min),chr(max))