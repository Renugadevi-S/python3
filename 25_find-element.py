#To find the given number is in list or not
#Usinf function

lis=[]
num=(input("enter numbers"))
lis.append(num)
print(lis)
def group_data(lis,n):
    for elements in lis:
        if n==elements:
         return True
    return False
print(group_data(lis,4))


