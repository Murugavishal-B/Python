user_input=input("Enter a list :")
list=[int(x) for x in user_input.split()]
print("Your List =",list)
min_value=list[0]
for i in list:
    if i<min_value:
        min_value=i
print("Minimum Value=",min_value)

