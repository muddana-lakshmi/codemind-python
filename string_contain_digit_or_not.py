a=input()
c=0
for i in a:
    if i.isdigit()==True:
        c+=1
if c==0:
    print("Doesn't contain digit")
else:
    print('Contains',c,'digit')