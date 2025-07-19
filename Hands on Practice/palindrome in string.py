s=input("Enter a String:")
s=s.lower()
rv=s[::-1]
if s==rv:
    print("Palindrome")
else:
    print("Not Palindrome")
