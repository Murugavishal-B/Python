text = input("Enter a string:")
words = text.split()
org=[]
dup=[]
for i in words:
    if i not in org:
        org.append(i)
    else:
        dup.append(i)
        break
print(' '.join(dup))
