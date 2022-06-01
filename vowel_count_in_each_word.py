n=input()
n=n.split()
for i in n:
    c=0
    k=[char for char in i]
    for j in k:
        if j in 'aeiouAEIOU':
            c+=1
    print(c,end=' ')