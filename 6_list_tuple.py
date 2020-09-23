#program which accepts a sequenceof comma-separatednumbers from user
#and generate a list and a tuple withthose numbers
inpt=(input(""))
lis=[]
lis.append(str(inpt))
lis=inpt.split(",")
print(lis)
tup=tuple(lis)
print(tup)
