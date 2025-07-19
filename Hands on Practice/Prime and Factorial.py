def getval():
    num=int(input("Enter a Number:"))
    return num
def prime(n):
    for i in range(2,n):
        if(n%2==0):
            return "is not a Prime Number"
    else:
        return "is a Prime Number"
def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)
n=getval()
print(n,prime(n))
print(f"Factorial of {n} is:{fact(n)}")
