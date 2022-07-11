s=input()
r=[]
for i in s:
    if i in 'aeiouAEIOU':
        r.append(i)
print(len(r))