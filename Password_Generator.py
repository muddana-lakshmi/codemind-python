s=str(input())
l=s.split(',')
r=[]
m=0
for i in l:
    x=0
    m=0
    k=i.index(":")
    for j in range(len(i)):
        if i[j] in '0123456789':
            if int(i[j])>m and int(i[j])<=k:
                m=int(i[j])
    for j in range(len(i)):
        if j==m-1:
            if (i[j] not in '0123456789') and (i[j]!=':'):
                x+=1
                r.append(i[j])
                break
    if(x==0):
        r.append("X")
for i in r:
    print(i,end='')