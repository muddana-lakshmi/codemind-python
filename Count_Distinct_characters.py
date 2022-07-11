s=input()
s=s.lower()
k=[]
x=0
for i in s:
    if i not in k:
        k.append(i)
r=[]
for i in k:
    if i not in r:
        if i!=' ':
            r.append(i)
print(len(r))