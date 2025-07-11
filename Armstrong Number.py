n=input("Enter a Number:")
digit=len(n)
s=0
for i in n:
    s+=(int(i)**digit)
if s==int(n):
    print("Armstrong")
else:
    print("Not Armstrong")
