s=input()
s=s.split(' ')
r=[]
for i in s:
    i=list(i)
    if i[0] in 'AEIOUaeiou':
        i.append('m')
        i.append('a')
    else:
        k=i[0]
        i.remove(k)
        i.append(k)
        i.append('m')
        i.append('a')
    r.append(i)
t=[]
for i in range(len(r)):
    for j in range(0,i+1):
        r[i].append('a')
    t.append(r[i])
for i in t:
    for j in i:
        print(j,end='')
    print(' ',end='')
    