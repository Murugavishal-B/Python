user_input=input("Enter a List :")
list=[int(x) for x in user_input.split()]
print("Your List=",list)
chord_element=int(input("Insert a Chord in your list:"))
position=int(input("Enter Your Position of Chord:"))
list.insert(position,chord_element)
print(list)
