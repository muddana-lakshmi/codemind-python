n=input()
a=input()
n=n.lower()
a=a.lower()
a=a.split()
n=n.split()
s=[]
for i in a:
    c=0
    if i in n:
        c+=1
    if c>=1:
        s.append(i)
print(*s)
        