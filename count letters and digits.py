para=input("Enter a Paragraph:")
l,d=0,0
for i in para:
    if i.isalpha():
        l+=1
    elif i.isdigit():
        d+=1
print(f"Letters={l}\nDigits={d}")
