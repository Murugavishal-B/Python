try:
    age = int(input("Enter your age:"))
    if age > 18:
        print("You are eligible to vote.")
    else:
        print("You are not eligible to vote.")
except:
    print("lnvalid input! Please enter a valid age.")
