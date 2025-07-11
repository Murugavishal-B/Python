def fibo(n,a=0,b=1):
    if n==0:
        return [ ]
    return [a]+fibo(n-1,b,a+b)
n=int(input("Enter  Number of Terms:"))
print(fibo(n))
