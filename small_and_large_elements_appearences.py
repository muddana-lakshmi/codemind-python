s=input()
min=999
max=0
r=[]
for i in s:
    if i!=' ':
        r.append(i)
for i in r:
    if ord(i)<min:
        min=ord(i)
    if ord(i)>max:
        max=ord(i)
print(chr(min),r.count(chr(min)),chr(max),r.count(chr(max)))