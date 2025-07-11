para=input("Enter a Paragraph:")
words=para.split()
cap_words=[x.capitalize() for x in words]
for i in cap_words:
    print(i,end=" ")
