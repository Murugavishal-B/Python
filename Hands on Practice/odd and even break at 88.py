n=int(input("Enter a Number:"))
Even=[ ]
Odd=[ ]
for i in range(1,n+1):
    if i%2==0:
        if i==88:
            break
        else:
            Even.append(i)
    else:
        Odd.append(i)
print("Even=",Even)
print("Odd=",Odd)
