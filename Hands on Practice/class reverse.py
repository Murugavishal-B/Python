class reverse:
    def rev(self,string):
        words=string.split()
        rev_words=words[::-1]
        for i in rev_words:
            print(i,end=" ")
string=input("Enter a String:")
reverse().rev(string)
