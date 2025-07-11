s=input("Enter a string:")
r=int(input("Enter the index vaule to remove:"))
if r<0 or r>len(s):
    print("Invallid Index")
else:
    print(f"After removing:{s[:r]+s[r+1:]}")
