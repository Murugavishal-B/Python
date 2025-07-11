f=int(input("Enter the final value:"))
a,b=0,1
for i in range(f):
    print(a,end=" ")
    a,b=b,a+b
    if a>f:
        break
