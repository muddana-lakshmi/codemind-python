a=input()
words=a.split()
sen=[word[::-1] for word in words]
print(" ".join(sen))