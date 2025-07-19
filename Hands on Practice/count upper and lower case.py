s=input("Enter a String:")
up,lr=0,0
for i in s:
    if i.isupper():
        up+=1
    elif i.islower():
        lr+=1
print(f"Uppercase={up}\nLowercase={lr}")
