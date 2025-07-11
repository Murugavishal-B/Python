str1=input("Enter a String:")
str1=str1.lower()
count=0
for i in str1:
    if i=='a'or 'e' or 'i' or 'o' or 'u':
        count+=1
print(count)
