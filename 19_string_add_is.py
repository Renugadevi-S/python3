#Python program to get a new string from a given string where "Is" has been added to the front.
#If the given string already begins with "Is" then return the string unchanged

def string(str1):
    if str1[0:2]=="is":
        return str1
    return "is"+str1
print(string("a beautiful world"))
print(string("is this is you"))
    
