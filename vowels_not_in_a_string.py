s=input()
r=[]
for i in s:
    if i in 'aeiou':
        r.append(i)
w=[]
if 'a' not in r:
    w.append('a')
if 'e' not in r:
    w.append('e')
if 'i' not in r:
    w.append('i')
if 'o' not in r:
    w.append('o')
if 'u' not in r:
    w.append('u')
if w==[]:
    print(0)
else:
    print(*w)
    