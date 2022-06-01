n=input()
n=n.split()
l=[]
for i in n:
    c=0
    k=[char for char in i]
    for j in k:
        if j in 'aeiouAEIOU':
            c+=1
    l.append(c)
print(min(l))