l=[1,2,3,6,5,4,1,3,2]
dup=[]
org=[]
for i in l:
    if i not in org:
        org.append(i)
    else:
        dup.append(i)
print(sorted(org))
