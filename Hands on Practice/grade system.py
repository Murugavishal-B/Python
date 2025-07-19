m1=int(input("Enter Mark1:"))
m2=int(input("Enter Mark2:"))
m3=int(input("Enter Mark3:"))
per=((m1+m2+m3)/300)*100
print("Your Percentage:",per)
if(per>90 and per<=100):
    print("Grade:A")
elif(per>80 and per<=90):
    print("Grade:A1")
elif(per>70 and per<=80):
    print("Grade:B")
elif(per>60 and per<=70):
    print("Grade:B1")
elif(per>50 and per<=60):
    print("Grade:C")
else:
    print("Sorry You Failed")
