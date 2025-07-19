start=int(input("Enter a Starting of Range:"))
end=int(input("Enter a Ending of Range:"))
for i in range(start,end+1):
    print(i,end=" ")
guess=int(input("\nEnter a Number to Guess in a Range:"))
if guess in range(start,end+1):
    print(guess,"is in Range")
else:
    print(guess,"is not in Range")
