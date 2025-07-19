def right_angle_triangle(a,b,c):
    sides=sorted([a,b,c])
    if sides[2]**2==sides[0]**2+sides[1]**2:
        print("It's a Right Angle Triangle")
    else:
        print("It's is not a Right Angle Triangle")
a=float(input("Enter the first Side:"))
b=float(input("Enter the second Side:"))
c=float(input("Enter the Third Side:"))
right_angle_triangle(a,b,c)
