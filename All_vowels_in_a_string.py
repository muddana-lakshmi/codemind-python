s=input()
x=0
y=0
if 'a' in s:
    x+=1
if 'e' in s:
    x+=1
if 'i' in s:
    x+=1
if 'o' in s:
    x+=1
if 'u' in s:
    x+=1
if 'A' in s:
    y+=1
if 'E' in s:
    y+=1
if 'I' in s:
    y+=1
if 'O' in s:
    y+=1
if 'U' in s:
    y+=1
if x==5 or y==5:
    print("True")
else:
    print("False")