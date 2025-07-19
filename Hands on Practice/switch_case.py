def cal(ch,a,b):
    a,b=sorted([a,b])
    if ch=="add":
        print(a+b)
    elif ch=="sub":
        print(a-b)
ch=input("Enter Ch:")
a=int(input("Enter a:"))
b=int(input("Enter b:"))
