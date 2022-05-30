n=input()
c=0
x=0
y=0
z=0
for i in n:
    if i in "aeiouAEIOU":
        c+=1
    if i in 'bcdjklmnpqrstvwxyzfghBCDFGHJKLMNPQRSTVWXYZ':
            x+=1
    if i==' ':
        y+=1
    if i in '1234567890':
        z+=1
print("Vowels:",c)
print("Consonants:",x)
print("Digits:",z)
print("White spaces:",y)
